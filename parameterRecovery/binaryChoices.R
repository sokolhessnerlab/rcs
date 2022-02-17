# Function that changes probabilities into binary choices (1= accept gamble, 0 = reject) 
# Risk, context and strategy study
# Hayley Brooks
# 02/17/22

binaryChoiceFromProb <- function(choiceProb) {
  # code from PSH CLASE study
  
  binaryChoices = choiceProb > runif(length(choiceProb));
  # If 'p' value is low, e.g. 0.2, then it will only be greater 
  # than a random number uniformly-distributed between 0 and 1
  # 20% of the time, that is, with p = 0.2
  binaryChoices = as.numeric(binaryChoices);
  
  return(binaryChoices)
}