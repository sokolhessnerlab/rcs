# Function that constains lambda to =1 (gain-only task) for the probability function
# Hayley Brooks
# 02/17/21


conLprob<-function(parameterVals, choiceset){
  prob <- ptProb(c(1,parameterVals), choiceset) #need to give ptLL 2 inputs: parameter values and choiceset
  return(prob)
};

