# Function for the parameter recovery exercise for temporal context
# sets up bounds, initiatl parvals, optim, etc.

rcsTempContextParRec <- function(n,subjdata){
  alloutput <- list() # Prepare the object into which we're going to put all the outputs of each iteration
  for(i in 1:n){ # n is iteration for each core
    alloutput[[i]] <- NA
    
    trialLevel = glm(choice ~ gainSC + altSC + grndEVscaled, data=subjdata, family="binomial")
    subjdata$preds = predict(trialLevel,type = "link")
    
    tempContext = glm(choice ~ 0 + earningsSC*poc1scaled + trialSC*poc1scaled + shiftDiffscPOS, data=mriBehClean, family="binomial", offset=pred)); # before testing this, need to add trial, poc, earnings to the choiceset
    

    alloutput[[i]] <-trialLevel
  };
  return(alloutput) # return big list
#return(trialLevel)
};


exampleChoiceDF$gainSC = round(exampleChoiceDF$riskyGain/61, digits=2)
exampleChoiceDF$altSC = round(exampleChoiceDF$alternative/61, digits=2)
exampleChoiceDF$grndEVscaled = round(exampleChoiceDF$evLevel/61, digits=2)
exampleChoiceDF$choice = exampleChoiceDF$exampleChoice
x = rcsTempContextParRec(10,exampleChoiceDF)

# 2/28
# Overall, terrible recovery for the first round. The majority of recovered values are hitting the bounds (looking at histograms)
# for past outcome, bounds are both at -.2 and .5 (over 6000 at each bound)
# for shift, ~8000 were at the lower bound .5, and ~5000 were at the upper bound of 4
# for earnings, over 16000 at the .10 bound
# going to change the range of possible values

# meeting with PSH 3/4: using glmer instead of optim
# this should include the two step approach
# try two independent GLMs without giving starting values and check output. Did this for the trial-level and the results were identical.


# then, consider setting initial values for the three values we want to recover (can set the others to 0)
# set initial values using 'start' in glm and the values will be from a uniform distribution centered around 0
# DONT FORGET THE CONSTANT!




# 
# rcsTempContextParRec <- function(n,subjdata){
#   alloutput <- list() # Prepare the object into which we're going to put all the outputs of each iteration
#   for(i in 1:n){ # n is iteration for each core
#     lb = c(-2,0,-1); # poc, shift, earnings
#     ub = c(2, 10, 10);  # poc, shift, earnings
#     initparval =  c(runif(1,-1.5,.5),runif(1,.5,3), runif(1,.1,2))
#     alloutput[[i]] <- NA
#     try({output = optim(initparval, tempContextLL, choiceset=subjdata, method= "L-BFGS-B", lower=lb, upper=ub,hessian=TRUE); #using tempContextLL function
#     alloutput[[i]] <- output}); # Save the output into a bigass list
#   };
#   return(alloutput) # return big list
# };