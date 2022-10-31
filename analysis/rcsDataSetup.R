# Set up data for analysis for RCS (HRB's dissertation study)
# October 18, 2022
# Hayley Brooks

# clear global environment
rm(list=ls())

config = config::get()
library(dplyr)
library(readr)
library(lme4)


# load data frames that were saved in during QA(rcsDataQA.Rmd)
load(file.path(config$path$data$Rdata,'rdmDF_clean.Rdata'))
load(file.path(config$path$data$Rdata, 'RDMqualityCheck.Rdata'))
load(file.path(config$path$data$Rdata, 'ospan_clean.Rdata'))
load(file.path(config$path$data$Rdata, 'symspan_clean.Rdata'))
load(file.path(config$path$data$Rdata, 'ERQscores.Rdata'))
conditionsFile = read_csv('/Users/hayley/Documents/GitHub/rcs/task/rdmTask/rcsConditions.csv')


# set up subject ID variables (using dataframe that has exclusion already applied)
subIDchar = unique(rdmDFclean$subID)
nSub = length(subIDchar)
excludeSubID = c("012", "015", "022", "028")



# create a variable for condition code
# 1 = control, control
# 2 = control, strategy
# 3 = strategy, control
# 4 = strategy, strategy


conditionsFile = conditionsFile[!conditionsFile$subID %in% excludeSubID,] # this applies exclusion
conditionsFile = conditionsFile[1:nSub,] # just include current participants up until this point



# create variables for glmer
scaleby = max(rdmDFclean$riskyGain, na.rm=T)# most variables will be scaled by this

rdmDFclean$evLevScaled = rdmDFclean$evLevel/scaleby


# Create a function that creates recent event variables for RCS dataset:
rcs_past_event_variable <- function(DFname, DFwithVariable, trialsBack, DFwithSubID, DFwithRound, scaled){
  # DFname = name of the dataframe
  # DFwithVariable = full name of dataframe + variable name that we want to shift (e.g. rdmDFclean$outcome)
  # trialsBack = numeric; how many trials are we look back?
  # DFwithSubID = full name of dataframe + sub id variable (e.g. rdmDFclean$subID)
  # DFwithRound = full name of dataframe + phase variable (e.g. rdmDFclean$round)
  # scaled = 1 = yes, 0 = no (scaled by max risky gain amount)
  
  newMat = as.data.frame(matrix(data=NA,nrow=nrow(DFname), ncol=4), dimnames=list(c(NULL), c("newVar", "subDiff", "roundDiff")));
  
  newMat$newVar <- DFwithVariable; #take data from columns
  newMat$newVar[(trialsBack + 1):nrow(newMat)] <- newMat$newVar[1:(nrow(newMat)-trialsBack)]; # removes first row, shifts everything up
  newMat$newVar[1:trialsBack] <- NaN #put Nan in for rows that we shifted everything back by
  
  newMat$subDiff<-c(0,diff(DFwithSubID)); #note when sub ID changes
  newMat$roundDiff<-c(0,diff(DFwithRound)); # note when round changes
  
  
  subIDchange = which(newMat$subDiff!=0); # where there is a subject id change
  roundchange = which(newMat$roundDiff!=0); # where there is a round change
  
  newMat$newVar[subIDchange] = NaN
  newMat$newVar[roundchange] = NaN
  
  if(trialsBack>1){ # if we want to go back more than one trial
    for (t in 1:(trialsBack-1)) {
      newMat$newVar[subIDchange+t] = NaN
      newMat$newVar[roundchange+t] = NaN
    }
  }
  
  return(newMat$newVar)
}

# create recent event variables

# past outcome
rdmDFclean$pastOC1 = rcs_past_event_variable(rdmDFclean,rdmDFclean$outcome, 1, as.numeric(rdmDFclean$subID),rdmDFclean$roundRDM, 0); # outcome t-1
rdmDFclean$pastOC1sc = rdmDFclean$pastOC1/scaleby

# create variables for shift analysis
rdmDFclean$signedShift = c(0, diff(rdmDFclean$evLevel));
rdmDFclean$signedShift[rdmDFclean$rdmTrial==1] = 0; # first trial is always 0
rdmDFclean$posShift = rdmDFclean$signedShift*as.numeric(rdmDFclean$signedShift>0);
rdmDFclean$negShift = rdmDFclean$signedShift*as.numeric(rdmDFclean$signedShift<0);


# earnings rel. expectations.

# Calculate cumulative earnings (within each round) for each participant and scale expectations so that it is 0-1 for each participant
# earnings will be 0 to 1, normalized by each participant's max earnings
# save the max cumulative earnings for each person in a vector

earningsByRound = vector(); # to store all earnings for each participant
earningsByRoundScaled = vector(); # to store earnings scaled by each participants' max earnings within each round
trialByRound = vector(); # to store scaled trial for each participant

maxEarnSubRound= as.data.frame(matrix(data=NA, nrow = nSub, ncol = 3, dimnames=list(c(NULL), c("subID","maxEarnRound1", "maxEarnRound2"))));
maxEarnSubRound$subID = 1:nSub;


for (s in 1:nSub) {
  sub = rdmDFclean[rdmDFclean$subID==subIDchar[s],]
  earningsSub = vector(); # reset earnings vector for each participant
  trialScaled = vector(); # reset trial vector for each participant
  earningsSubScaled = vector(); # reset scaled earnings vector for each participant
  
  
  
  earningsSub = c(cumsum(sub$outcome[sub$roundRDM==1]), cumsum(sub$outcome[sub$roundRDM==2]));
  trialScaled = c(sub$trial[sub$roundRDM==1]/max(sub$trial[sub$roundRDM==1]),sub$trial[sub$roundRDM==2]/max(sub$trial[sub$roundRDM==2]));
  maxEarnSubRound$maxEarnRound1[s] = max(cumsum(sub$outcome[sub$roundRDM==1]));
  maxEarnSubRound$maxEarnRound2[s] = max(cumsum(sub$outcome[sub$roundRDM==2]));
  
  earningsSubScaled = c(cumsum(sub$outcome[sub$roundRDM==1])/max(cumsum(sub$outcome[sub$roundRDM==1])), cumsum(sub$outcome[sub$roundRDM==2])/max(cumsum(sub$outcome[sub$roundRDM==2])));
  
  earningsByRound = c(earningsByRound,earningsSub);
  trialByRound = c(trialByRound,trialScaled);
  earningsByRoundScaled = c(earningsByRoundScaled,earningsSubScaled)
  
}


rdmDFclean$earnings = earningsByRound;
rdmDFclean$earnNormalized01 = earningsByRoundScaled; # 0-1 (normalized within sub)
rdmDFclean$trialSC = trialByRound;
rdmDFclean$earnNormalizedOverall = rdmDFclean$earnings/max(rdmDFclean$earnings) # scale by max earnings overall

# quick summary about cumulative earnings:
# round 1: range = $1576 - $2467, median = $2096, mean = $2091
# round 2: range = $1597 - $2492, median = $2103, mean = $2118



# recode strategy (its currently 01, recode to be -1 and 1)
rdmDFclean$strategyRecode = rdmDFclean$strategy
rdmDFclean$strategyRecode[rdmDFclean$strategyRecode==0] =-1



rdmDFclean$subIDnum = as.numeric(rdmDFclean$subID)

# recode round (current 1 and 2, recode to - and 1)
rdmDFclean$roundRecode = rdmDFclean$roundRDM
rdmDFclean$roundRecode[rdmDFclean$roundRecode == 1] = -1
rdmDFclean$roundRecode[rdmDFclean$roundRecode == 2] = 1
