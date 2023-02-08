// This Stan program defines a simple model, with a
// vector of values 'y' modeled as normally distributed
// with mean 'mu' and standard deviation 'sigma'.
//
// Learn more about model development with Stan at:
//
//    http://mc-stan.org/users/interfaces/rstan.html
//    https://github.com/stan-dev/rstan/wiki/RStan-Getting-Started
//

// Stan program has 3 required blocks: data, parameters, and model. There are additional blocks: functions, transformed data, transformed parameters, generated quantities


//DONT FORGET SEMI COLONS!!

// real = has decimals - also has to do with math that will happen during fitting
//int = 0 or 1, or single number - int can be used in loops

// The input data is a vector 'y' of length 'N'.
data {
  int N; // number of trials (across participants)
  int nsubj; // number of participants
  int choices[N]; // choice vector
  real gain[N]; // risky gain vector
  real safe[N]; // safe vector
  real poc[N]; // past outcome vector
  int ind[N]; // subject index
}

// The parameters accepted by the model. Our model
// accepts two parameters 'mu' and 'sigma'.

 // parameters is just for defining the parameters and what they are (e.g. real) and setting limits if necessary (esp for sd)
parameters {
  real meanRho;
  real<lower=0> sdRho;
  real meanMu;
  real<lower=0> sdMu;
  real meanDB;
  real<lower=0> sdDB;
  
  real meanPocAdjDB; // Decision bias adjustment
  real<lower=0> sdPocAdjDB;
  real meanPocAdjR; // Rho adjustment
  real<lower=0> sdPocAdjR;
  real meanPocAdjM; // Mu adjustment
  real<lower=0> sdPocAdjM;
  
  real r[nsubj]; // random effects for rho
  real m[nsubj]; // random effects for mu
  real db[nsubj]; // random effects for decision bias
  real pocAdjDB[nsubj]; // random effects for decision bias poc adjustment
  real pocAdjR[nsubj]; // random effects for rho poc adjustment
  real pocAdjM[nsubj]; // random effects for mu poc adjustment
  
}

// transformed parameters - where a lot of the work actually happens, esp as we modify the model.

transformed parameters {
  real rtmp[N];
  real mtmp[N];
  real dbtmp[N];
  real pocAdjDBlim[nsubj];
  real pocAdjRlim[nsubj];
  real pocAdjMlim[nsubj];
  
  for(s in 1:nsubj){
    pocAdjDBlim[s] = 1/(1+exp(-pocAdjDB[s]))*2-1;
    pocAdjRlim[s]  = 1/(1+exp(-pocAdjR[s]))*2-1;
    pocAdjMlim[s]  = 1/(1+exp(-pocAdjM[s]))*2-1;
  }
  
  // because we are adjusting on past outcome, we do slightly different things for first vs. the rest of the trials
  rtmp[1] = exp(r[ind[1]]); // take individual-level rho sample (that was sampled in unbounded space) and put it in the exponential to make it >0
  mtmp[1] = exp(m[ind[1]]); // same as above
  dbtmp[1] = db[ind[1]]; // db is not transformed
  
  for(t in 2:N){ // for each trial starting with trial 2
    if(ind[t]!=ind[t-1]){
      dbtmp[t]   = db[ind[t]];
      rtmp[t] = exp(r[ind[t]]); 
      mtmp[t] = exp(m[ind[t]]);
    } else {
      dbtmp[t]    = dbtmp[t-1]     + poc[t]*pocAdjDBlim[ind[t]];
      rtmp[t] = exp(log(rtmp[t-1]) + .25*poc[t]*pocAdjRlim[ind[t]]);
      mtmp[t] = exp(log(mtmp[t-1]) + .25*poc[t]*pocAdjMlim[ind[t]]);
    }
  }
}

// The model to be estimated. We model the output
// 'y' to be normally distributed with mean 'mu'
// and standard deviation 'sigma'.
// priors- need to set this up for everything defined in the parameters section EXCEPT the random effects 
model {
  real div;
  real p[N];
  //real gambleUtil; will try vector based stuff below but just in case there is an issue, not defining with N might work better.
  //real safeUtil;
  real gambleUtil; // utility for gamble (with losses, this would need to be utility of gain and loss)
  real safeUtil; // utility for safe option
  
  //Priors
  meanRho ~ normal(0,30);
  sdRho ~ cauchy(0,2.5);
  meanMu ~ normal(0,30);
  sdMu ~ cauchy(0,2.5);
  meanDB ~ normal(0,30);
  sdDB ~ cauchy(0,2.5);
  meanPocAdjDB ~ normal(0,10);
  sdPocAdjDB ~ cauchy(0,2.5);
  meanPocAdjR ~ normal(0,10);
  sdPocAdjR ~ cauchy(0,2.5);
  meanPocAdjM ~ normal(0,10);
  sdPocAdjM ~ cauchy(0,2.5);


  //Hierarchy
  r ~ normal(meanRho, sdRho);
  m ~ normal(meanMu, sdMu);
  db ~ normal(meanDB,sdDB);
  pocAdjDB ~ normal(meanPocAdjDB, sdPocAdjDB);
  pocAdjR ~ normal(meanPocAdjR, sdPocAdjR);
  pocAdjM ~ normal(meanPocAdjM, sdPocAdjM);

  for (t in 1:N) {
    div = 61^rtmp[t];
    // Model with M, R, DB
    gambleUtil = 0.5 * gain[t]^rtmp[t];

    safeUtil = safe[t]^rtmp[t];
    

    p[t] = inv_logit(mtmp[t] / div * (gambleUtil - safeUtil - dbtmp[t]));
    
    if (is_nan(p[t])){
      print("parameter set:");
      print(mtmp[t]);
      print(rtmp[t]);
      print(dbtmp[t]);
    }

  }
  choices ~ bernoulli(p);
}
