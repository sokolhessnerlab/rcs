# Function that constrains lambda to 1 for Prospect Theory (gain-only task) for negative log likelihood function
# Hayley Brooks
# 02/17/22


conL<-function(parameterVals, choiceset){
  ll <- ptLL(c(1,parameterVals), choiceset) #need to give ptLL 2 inputs: parameter values and choiceset
  return(ll)
};
