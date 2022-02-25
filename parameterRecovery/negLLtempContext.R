# Function to change probabilities into negative log likelihoods from temporal context PR (temporalContextProbChoice.R)
# Risk, context and strategy study
# Hayley Brooks
# 02/24/22

tempContextLL <-function(parameterVals, choiceset){ 
  eps = .Machine$double.eps;
  
  source('temporalContextProbChoice.R')
  
  choiceProb = contextProbChoices(parameterVals, choiceset); # choiceProb will have two columns: probabilities and binary choices
  choices = choiceProb[,1];
  probs = choiceProb[,2];
  
  # choiceProb[choiceProb==1]=1-eps;#indexing, any number in prob that equals 1, set it to 1-eps
  # choiceProb[choiceProb==0]=eps; #indexing, any number in prob that equals 0, set it to eps
  
  ll <- sum(log(choices*probs + (1-choices)*(1-probs))); #find the log likelihood 
  nll = -ll; # because the log of a number between 0 and 1 is negative (making the log likelihood
  # a negative number that we'd have to maximize (i.e. make the least negative possible), 
  # and most estimation procedures ask for MINIMIZATION problems, we take the negative to flip this, 
  # allowing us to MINIMIZE the NEGATIVE log likelihood
  
  return(nll);
}