# Function to change probabilities into negative log likelihoods from the PT model (choiceProbabilityProspectTheory.R)
# Risk, context and strategy study
# Hayley Brooks
# 02/17/22

ptLL <-function(parameterVals, choiceset){ 
  eps = .Machine$double.eps;
  
  source('choiceProbabilityProspectTheory.R')

  choiceProb = ptProb(parameterVals, choiceset);
  
  
  choiceProb[choiceProb==1]=1-eps;#indexing, any number in prob that equals 1, set it to 1-eps
  choiceProb[choiceProb==0]=eps; #indexing, any number in prob that equals 0, set it to eps
  
  ll <- sum(log(choiceset$choices*choiceProb + (1-choiceset$choices)*(1-choiceProb))); #find the log likelihood 
  nll = -ll; # because the log of a number between 0 and 1 is negative (making the log likelihood
# a negative number that we'd have to maximize (i.e. make the least negative possible), 
# and most estimation procedures ask for MINIMIZATION problems, we take the negative to flip this, 
# allowing us to MINIMIZE the NEGATIVE log likelihood
  
return(nll);
}