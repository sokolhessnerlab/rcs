# Function for the parameter recovery exercise for temporal context
# sets up bounds, initiatl parvals, optim, etc.


rcsTempContextParRec <- function(n,subjdata){
  alloutput <- list() # Prepare the object into which we're going to put all the outputs of each iteration
  for(i in 1:n){ # n is iteration for each core
    alloutput[[i]] <- NA
    
  
    trialLevelInit = c(runif(1,-3,3),runif(1,-3,3),runif(1,-3,3),runif(1,-3,3)); # four to include the constant
    trialLevel = glm(choice ~ gainSC + altSC + grndEVscaled, data=subjdata, family="binomial", start = trialLevelInit) 
    
    subjdata$preds = predict(trialLevel,type = "link")
    
    pred = predict(trialLevel, type="link")
    
    tempContextInit = c(runif(1,-2,2), runif(1,-2,2), runif(1, -2,2),0,0,0)
    tempContext = glm(choice ~ 0 + earningsSC*poc1scaled + expectSC*poc1scaled + shiftDiffscPOS, data=subjdata, family="binomial", offset=pred, start=tempContextInit); # before testing this, need to add trial, poc, earnings to the choiceset
    

    alloutput[[i]] <-tempContext
  };
  return(alloutput) # return big list
#return(trialLevel)
};



#choiceset =rcsChoiceSet();
#parameterVals = c(-0.9415, 1.5829, 0.4419);
#choiceset = contextProbChoices(parameterVals, choiceset)
#output = rcsTempContextParRec(20, choiceset)


# 2/28
# Overall, terrible recovery for the first round. The majority of recovered values are hitting the bounds (looking at histograms)
# for past outcome, bounds are both at -.2 and .5 (over 6000 at each bound)
# for shift, ~8000 were at the lower bound .5, and ~5000 were at the upper bound of 4
# for earnings, over 16000 at the .10 bound
# going to change the range of possible values

# meeting with PSH 3/4: using glmer instead of optim
# this should include the two step approach
# try two independent GLMs without giving starting values and check output. Did this for the trial-level and the results were identical. Similary for temporal context, the output is identical.


# Next --> set initial values for the three values we want to recover (can set the others to 0). Was getting the same results if I didn't set the initial values for the trial level glm. Seemed like most reasonable results were uniformed distribution centered on zero with min and max = 2 or 3
# set initial values using 'start' in glm and the values will be from a uniform distribution centered around 0
# DONT FORGET THE CONSTANT!




#