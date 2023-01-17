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
  
  real r[nsubj]; // random effects for rho
  real m[nsubj]; // random effects for mu
}

// transformed parameters - where a lot of the work actually happens, esp as we modify the model.

transformed parameters {
  real rtmp[N];
  real mtmp[N];
  
  for(t in 1:N) { // for each trial
    rtmp[t] = exp(r[ind[t]]); // take individual-level rho sample (that was sampled in unbounded space) and put it in the exponential to make it >0
    mtmp[t] = exp(m[ind[t]]); // same as above for mu
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
  real gambleUtil[N]; // utility for gamble (with losses, this would need to be utility of gain and loss)
  real safeUtil[N]; // utility for safe option
  
  //Priors
  meanRho ~ normal(0,30);
  sdRho ~ cauchy(0,2.5);
  meanMu ~ normal(0,30);
  sdMu ~ cauchy(0,2.5);
  
  //Hierarchy
  r ~ normal(meanRho, sdRho);
  m ~ normal(meanMu, sdMu);
  
  for (t in 1:N) {
    div = 61^rtmp[t];

    // Model with M, L, R
    gambleUtil = 0.5 * gain[t]^rtmp[t];

    safeUtil = safe[t]^rtmp[t];

    p[t] = inv_logit(mtmp[t] / div * (gambleUtil - safeUtil));
  }
  choices ~ bernoulli(p); 
}
