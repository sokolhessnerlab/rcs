# Temporal context function that generates probabilities and binary choices
# Risk, context and strategy study
# Hayley Brooks
# 02/23/22


contextProbChoices <-function(parameterVals, choiceset){ #parameterVals and choiceset are the two inputs this needs to work
  eps = .Machine$double.eps;
  
  nTri = nrow(choiceset); # number of trials
  
  # BETAS:
  # Define the regression betas that aren't input in the function
  # these are from the trial level model from VNI:
  gainBeta = 16.118 
  safeBeta = -41.078  
  meanEVBeta = 6.990

  # these are from the temporal context model from VNI (variables we aren't using to create subjects):
  expBeta  = -1.4531
  pocEarnBeta = 5.2010
  pocExpBeta = -2.8280
  
  # Betas we are using to create participants (which are also based on temporal context model from VNI)
  pocBeta = parameterVals[[1]]; #parameter 1 is past outcome beta
  shiftBeta = parameterVals[[2]]; #parameter 2, positive shift beta
  earnBeta = parameterVals[[3]]; #parameter 3 is relative earnings beta
  
  
  # DATA:
  scaleby = 61; # generated 4000 choiceset and the max riskyGain was 61 (range of max across choicesets was 59-61)
  
  
  gain = choiceset$riskyGain/scaleby;   # riskyGain column of given data, scale it
  safe = choiceset$alternative/scaleby; # alternative column of given data, scale it
  meanEV = choiceset$evLevel/scaleby;   # evLevel column of given data, scale it
  expectations = 1:nTri/nTri # scaled so that expectations increase linearly from 0-1
  shift = c(0,diff(choiceset$evLevel))/scaleby; # get shift difference scale by max(riskyGain)
  shift[shift<0] = 0; # we only want positive shift differences, zero out the negatives
  
  # set up our dynamic variables that change based on previous trial
  
  # for poc and earnings, the first trial will be 0
  poc = vector(mode="integer", length=nTri); 
  earnings = vector(mode="integer", length=nTri); 

  
  prob = vector(mode="integer",length=nTri); # for probabilities
  choices = vector(mode="integer", length=nTri); # for binary choices
  
  for(t in 1:nTri){ # for every trial
    
    # Probability of choosing the gamble:
    prob[t] = 1/(1+exp(-1*(gainBeta*gain[t] + safeBeta*safe[t] + meanEVBeta*meanEV[t] + pocBeta*poc[t] + shiftBeta*shift[t] + earnBeta*earnings[t] + expBeta*expectations[t] + pocEarnBeta*poc[t]*earnings[t] + pocExpBeta*poc[t]*expectations[t]))); 
    
    
    choices[t] = binaryChoiceFromProb(prob[t]); # generate binary choice from probability using our predefined function
    
    if(choices[t]==1){ # if risky gamble chosen,
      ranNum = rbinom(1, 1, 0.5); # generate 1 value (1 for win or 0 for loss) from binomial distribution with prob = .5
      poc[t+1] = (ranNum*gain[t])/scaleby; # past outcome is 1*riskyGain[t] (win) or 0*riskyGain[t] (losses are always 0). Scale it.
    } else {
      poc[t+1] = safe[t]/scaleby; # otherwise, past outcome is the safe option, scale it too.
    }
    
    earnings[t+1] = sum(poc)/66.75; 
    # earnings are the sum of past outcomes scaled by max(riskyGain), then scaled again by 66.75 which is max(earnings scaled) in VNI. We did this to make the VNI model run better and want to mimic exactly what we did to generate the beta estimates we are using for this parameter recovery exercise.
    
  }

  probChoices=cbind(prob,choices); # combine probability and choices to be one output argument
  
  return(probChoices);
};

