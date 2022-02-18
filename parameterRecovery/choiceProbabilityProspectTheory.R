# Prospect Theory Function that generates probabilities of accepting the gamble
# Risk, context and strategy study
# Hayley Brooks
# 02/17/22


ptProb <-function(parameterVals, choiceset){ #parameterVals and choiceset are the two inputs ptLL needs to work
  eps = .Machine$double.eps;
  
  lambda = parameterVals[[1]]; #paramter 1 is loss aversion
  rho = parameterVals[[2]]; #parameter 2, is risk aversion
  mu = parameterVals[[3]]; #parameter 3 is consistency across trials
  
  x = choiceset$riskyGain; #find x in the riskyGain column of given data
  y = choiceset$riskyLoss; #find y in riskyLoss column of given data
  z = choiceset$alternative; #find z in alternative column of given data
  
  divF = max(x)^rho; # find the max risky gain value, raise it to rho; decorrelates rho and mu
  
  gamble = ((x^rho)*.5)  + ((-lambda * (-y)^rho)*.5); #utility fx for gamble (gain and loss combined)
  guaranteed = (z^rho); #utility fx for alternative
  #prob = (1+exp(-mu*(gamble-guaranteed)))^-1; #probabilty of choosing gamble over alternative
  
  prob = (1+exp(-mu*(1/divF)* (gamble-guaranteed)))^-1; #probabilty of choosing gamble over alternative
  #divF normalizes the values to make mu more consistent because it will be less sensitive to magnitude, and less correlated with rho


  return(prob);
};
