// This Stan program is for a model with rho, mu, and decision bias with round and strategy changing DB


// Stan program has 3 required blocks: data, parameters, and model. There are additional blocks: functions, transformed data, transformed parameters, generated quantities


//DONT FORGET SEMI COLONS!!

// real = has decimals - also has to do with math that will happen during fitting
//int = 0 or 1, or single number - int can be used in loops

data {
  int N; // number of trials (across participants)
  int nsubj; // number of participants
  int choices[N]; // choice vector
  real gain[N]; // risky gain vector
  real safe[N]; // safe vector
  real poc[N]; // past outcome vector
  int ind[N]; // subject index
  real rdmRound[N]; // round of rdm task (-1 = round 1, +1 = round 2)
  real strategy[N]; // strategy (-1 = act natural; +1 = ignore context)
}


 // parameters is just for defining the parameters and what they are (e.g. real) and setting limits if necessary (esp for sd)
parameters {
  real meanRho;
  real<lower=0> sdRho;
  real meanMu;
  real<lower=0> sdMu;
  real meanDB;
  real<lower=0> sdDB;

  real r[nsubj]; // random effects for rho
  real m[nsubj]; // random effects for mu
  real db[nsubj]; // random effects for decision bias
  
  real roundDB;
  real stratDB;
  real roundxstratDB;
  
}

// transformed parameters - where a lot of the work actually happens, esp as we modify the model.

transformed parameters {
  real rtmp[N];
  real mtmp[N];
  real dbtmp[N];


  for(t in 1:N) { // for each trial
    rtmp[t] = exp(r[ind[t]]);
    mtmp[t] = exp(m[ind[t]]);
    dbtmp[t] = db[ind[t]] + rdmRound[t] * roundDB + 
                            strategy[t] * stratDB + 
                            rdmRound[t] * strategy[t] * roundxstratDB;
  } 
}

// The model to be estimated. We model the output
// 'y' to be normally distributed with mean 'mu'
// and standard deviation 'sigma'.
// priors- need to set this up for everything defined in the parameters section EXCEPT the random effects 
model {
  // real div;
  // real p[N];
  real total_value[N];
  //real gambleUtil; will try vector based stuff below but just in case there is an issue, not defining with N might work better.
  //real safeUtil;
  // real gambleUtil; // utility for gamble (with losses, this would need to be utility of gain and loss)
  // real safeUtil; // utility for safe option
  
  //Priors
  meanRho ~ normal(0,30);
  sdRho ~ cauchy(0,2.5);
  meanMu ~ normal(0,30);
  sdMu ~ cauchy(0,2.5);
  meanDB ~ normal(0,30);
  sdDB ~ cauchy(0,2.5);

  //psychologically plausible values for change in db
  roundDB ~ normal(0,5); 
  stratDB ~ normal(0,5);
  roundxstratDB ~ normal(0,5);


  //Hierarchy
  r ~ normal(meanRho, sdRho);
  m ~ normal(meanMu, sdMu);
  db ~ normal(meanDB,sdDB);


  for (t in 1:N) {
    // div = 61^rtmp[t]; // 1 because using scaled risky gain
    // Model with M, R, DB
    // gambleUtil = 0.5*gain[t]^rtmp[t];

    // safeUtil = safe[t]^rtmp[t];
    
    total_value[t] = mtmp[t] / (61^rtmp[t]) * (0.5*gain[t]^rtmp[t] - 
                                              safe[t]^rtmp[t] - 
                                              dbtmp[t]);
    // p[t] = inv_logit(mtmp[t] / div * (gambleUtil - safeUtil - dbtmp[t]));
  }
  
  // p = inv_logit(total_value);
  // 
  // choices ~ bernoulli(p);
  
  choices ~ bernoulli_logit(total_value);
}
