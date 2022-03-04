# Function for the parameter recovery exercise for temporal context
# sets up initial parvals, GLM, etc.


rcsTempContextParRec <- function(n,subjdata){
  alloutput <- list() # Prepare the object into which we're going to put all the outputs of each iteration
  for(i in 1:n){ # n is iteration for each core
    alloutput[[i]] <- NA
    
  
    trialLevelInit = c(runif(1,-3,3),runif(1,-3,3),runif(1,-3,3),runif(1,-3,3)); # four to include the constant
    trialLevel = glm(choice ~ gainSC + altSC + grndEVscaled, data=subjdata, family="binomial", start = trialLevelInit); # run trial level mode 
    
    subjdata$pred = predict(trialLevel,type = "link"); # save predicted values (residuals)
  
    # set initial values for the context variables we are interested in recovering. Earnings is first, POC is second, expectations are Third, and Shift is fourth followed by the two interactions.So we want to specify just the init values for 1, 2, and 4.
    tempContextInit = c(runif(1,-2,2), runif(1,-2,2), 0, runif(1, -2,2),0,0); 
    tempContext = glm(choice ~ 0 + earningsSC*poc1scaled + expectSC*poc1scaled + shiftDiffscPOS, data=subjdata, family="binomial", offset=pred, start=tempContextInit); # run the temporal context model
    

    alloutput[[i]] <-tempContext; # save the model 
  };
  return(alloutput) # return big list of model output
};




# meeting with PSH 3/4: using glmer instead of optim
# this should include the two step approach
# try two independent GLMs without giving starting values and check output. Did this for the trial-level and the results were identical. Similary for temporal context, the output is identical.


# Next --> set initial values for the three values we want to recover (can set the others to 0). Was getting the same results if I didn't set the initial values for the trial level glm. Seemed like most reasonable results were uniformed distribution centered on zero with min and max = 2 or 3
# set initial values using 'start' in glm and the values will be from a uniform distribution centered around 0
# DONT FORGET THE CONSTANT in the trial level model!



