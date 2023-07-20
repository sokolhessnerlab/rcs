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

# online:
load(file.path(config$path$data$Rdata,'rdmDFall_clean.Rdata')) # loads rdm, ospan, symspan, erq, post task/ post round qs
load(file.path(config$path$data$Rdata,'rcsSubLevelLongClean.Rdata')) # sublevel long
load(file.path(config$path$data$Rdata,'rcsSubLevelWideClean.Rdata')) # sublevel wide



# create subID variables 
subIDchar = unique(rdmDFclean$subID)
nSub = length(subIDchar)



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


# past outcome for stan (doesn't like NA, have to change NA to 0)
rdmDFclean$pocStan = rdmDFclean$pastOC1
rdmDFclean$pocStan[is.na(rdmDFclean$pocStan)] = 0;

rdmDFclean$pocStanScaled = rdmDFclean$pocStan/max(rdmDFclean$pocStan, na.rm=T); # create a scaled version of poc for stan
rdmDFclean$stanSafeScaled = rdmDFclean$safe/max(rdmDFclean$safe, na.rm=T)

# past choice
rdmDFclean$pastChoice = rcs_past_event_variable(rdmDFclean,rdmDFclean$choice, 1, as.numeric(rdmDFclean$subID),rdmDFclean$roundRDM, 0); # choice t-1
rdmDFclean$pastChoice[rdmDFclean$pastChoice==0] = -1


# past mean EV
rdmDFclean$pastMeanEV =rcs_past_event_variable(rdmDFclean,rdmDFclean$meanEVscaled, 1, as.numeric(rdmDFclean$subID),rdmDFclean$roundRDM, 0); # meanEV t-1


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
earningsAcrossRounds = vector();
trialAcrossRounds = vector()

maxEarnSubRound= as.data.frame(matrix(data=NA, nrow = nSub, ncol = 3, dimnames=list(c(NULL), c("subID","maxEarnRound1", "maxEarnRound2"))));
maxEarnSubRound$subID = 1:nSub;


for (s in 1:nSub) {
  sub = rdmDFclean[rdmDFclean$subID==subIDchar[s],]
  earningsSub = vector(); # reset earnings vector for each participant
  trialScaled = vector(); # reset trial vector for each participant
  earningsSubScaled = vector(); # reset scaled earnings vector for each participant
  earningsAcrossRoundsSub = vector();
  trialAcrossRoundsSub = vector();
  
  subOCround1 = sub$outcome[sub$roundRDM==1]
  subOCround2 = sub$outcome[sub$roundRDM==2]
  earningsSub = c(0,cumsum(subOCround1[1:length(subOCround1)-1]), 0, cumsum(subOCround2[1:length(subOCround2)-1]));
  trialScaled = c(sub$trial[sub$roundRDM==1]/max(sub$trial[sub$roundRDM==1]),sub$trial[sub$roundRDM==2]/max(sub$trial[sub$roundRDM==2]));
  maxEarnSubRound$maxEarnRound1[s] = max(cumsum(sub$outcome[sub$roundRDM==1]));
  maxEarnSubRound$maxEarnRound2[s] = max(cumsum(sub$outcome[sub$roundRDM==2]));
  
  
  earningsAcrossRoundsSub = c(0,cumsum(sub$outcome[1:length(sub$outcome)-1]))
  trialAcrossRoundsSub = 1:nrow(sub)/nrow(sub)
  
  earningsSubScaled = c(cumsum(sub$outcome[sub$roundRDM==1])/max(cumsum(sub$outcome[sub$roundRDM==1])), cumsum(sub$outcome[sub$roundRDM==2])/max(cumsum(sub$outcome[sub$roundRDM==2])));
  
  earningsByRound = c(earningsByRound,earningsSub);
  trialByRound = c(trialByRound,trialScaled);
  earningsByRoundScaled = c(earningsByRoundScaled,earningsSubScaled)
  earningsAcrossRounds = c(earningsAcrossRounds, earningsAcrossRoundsSub)
  trialAcrossRounds = c(trialAcrossRounds,trialAcrossRoundsSub)
  
}


rdmDFclean$earnings = earningsByRound;
rdmDFclean$earnNormalized01 = earningsByRoundScaled; # 0-1 (normalized within sub)
rdmDFclean$trialSC = trialByRound;
rdmDFclean$earnNormalizedOverall = rdmDFclean$earnings/max(rdmDFclean$earnings) # scale by max earnings overall
rdmDFclean$earningsAcrossRounds = earningsAcrossRounds/max(earningsAcrossRounds) # scale by max earnings overall
rdmDFclean$trialAcrossRounds = trialAcrossRounds

rdmDFclean$linExpectation = trialByRound;
rdmDFclean$linExpAcrossRounds = trialAcrossRounds;



# recode strategy (its currently 01, recode to be -1 and 1)
rdmDFclean$strategyRecode = rdmDFclean$strategy
rdmDFclean$strategyRecode[rdmDFclean$strategyRecode==0] =-1

rdmDFclean$subIDnum = as.numeric(rdmDFclean$subID) # make sub column of numeric type

# recode round (current 1 and 2, recode to - and 1)
rdmDFclean$roundRecode = rdmDFclean$roundRDM
rdmDFclean$roundRecode[rdmDFclean$roundRecode == 1] = -1
rdmDFclean$roundRecode[rdmDFclean$roundRecode == 2] = 1


# scale shift
rdmDFclean$posShiftsc = rdmDFclean$posShift/scaleby
rdmDFclean$negShiftsc = rdmDFclean$negShift/scaleby
rdmDFclean$signedShiftsc = rdmDFclean$signedShift/scaleby


# create past shift variables to test if shift effect goes back more than one trial
rdmDFclean$signedShift_1triback = rcs_past_event_variable(rdmDFclean,rdmDFclean$signedShiftsc, 1, as.numeric(rdmDFclean$subID),rdmDFclean$roundRDM, 0); 

rdmDFclean$posShift_1triback = rcs_past_event_variable(rdmDFclean,rdmDFclean$posShiftsc, 1, as.numeric(rdmDFclean$subID),rdmDFclean$roundRDM, 0); 
rdmDFclean$negShift_1triback = rcs_past_event_variable(rdmDFclean,rdmDFclean$negShiftsc, 1, as.numeric(rdmDFclean$subID),rdmDFclean$roundRDM, 0); 

# create numeric version of motivation variable
rdmDFclean$motivationNumeric = as.numeric(rdmDFclean$overallMotivation)/max(as.numeric(rdmDFclean$overallMotivation), na.rm = T)


rdmDFclean$ERQreappMeanSC = rdmDFclean$ERQreappraisalMean/max(rdmDFclean$ERQreappraisalMean, na.rm=T)
rdmDFclean$ERQsuppMeanSC = rdmDFclean$ERQsuppressionMean/max(rdmDFclean$ERQsuppressionMean, na.rm=T)

rdmDFclean$ERQreappSumSC = rdmDFclean$ERQreappraisalSum/max(rdmDFclean$ERQreappraisalSum, na.rm=T)
rdmDFclean$ERQsuppSumSC = rdmDFclean$ERQsuppressionSum/max(rdmDFclean$ERQsuppressionSum, na.rm=T)

# recode reappraisal and suppresion to be -1 to 1 because having reap be .3-1 doesn't allow us to look at the difference between high and low reappraisers
#plot(((rdmDFclean$ERQreappraisal-min(rdmDFclean$ERQreappraisal, na.rm = T))/28)*2-1)
rdmDFclean$reapSpan0sum = ((rdmDFclean$ERQreappraisalSum-min(rdmDFclean$ERQreappraisalSum, na.rm = T))/28)*2-1
rdmDFclean$suppSpan0sum = ((rdmDFclean$ERQsuppressionSum-min(rdmDFclean$ERQsuppressionSum, na.rm = T))/23)*2-1

rdmDFclean$reapSpan0mean = ((rdmDFclean$ERQreappraisalMean-min(rdmDFclean$ERQreappraisalMean, na.rm = T))/4.666667)*2-1
rdmDFclean$suppSpan0mean = ((rdmDFclean$ERQsuppressionMean-min(rdmDFclean$ERQsuppressionMean, na.rm = T))/3.875)*2-1


# create median split and tertile variables for high, moderate and low reapraisers

rcsSubLevelLong_clean$reapSpan0sum = ((rcsSubLevelLong_clean$ERQreappSum-min(rcsSubLevelLong_clean$ERQreappSum, na.rm = T))/28)*2-1
rcsSubLevelWide_clean$reapSpan0sum = ((rcsSubLevelWide_clean$ERQreappSum-min(rcsSubLevelWide_clean$ERQreappSum, na.rm = T))/28)*2-1

rcsSubLevelLong_clean$reapSpan0mean = ((rcsSubLevelLong_clean$ERQreappMean-min(rcsSubLevelLong_clean$ERQreappMean, na.rm = T))/4.666667)*2-1
rcsSubLevelWide_clean$reapSpan0mean = ((rcsSubLevelWide_clean$ERQreappMean-min(rcsSubLevelWide_clean$ERQreappMean, na.rm = T))/3.875)*2-1



# reappraisal SUM

medSplitSUM = median(rcsSubLevelWide_clean$reapSpan0sum, na.rm=T); # median split value
thirdSplitSUM = quantile(rcsSubLevelWide_clean$reapSpan0sum, probs=c(1/3, 2/3), na.rm=T); # give us lower and upper third quantiles

rdmDFclean$isHighReapSumMedSplit = as.numeric(rdmDFclean$reapSpan0sum >= medSplitSUM)
rdmDFclean$isLowReapSumMedSplit = as.numeric(rdmDFclean$reapSpan0sum < medSplitSUM)

rdmDFclean$highLowReapSumMedSplit = rdmDFclean$isHighReapSumMedSplit
rdmDFclean$highLowReapSumMedSplit[rdmDFclean$isLowReapSumMedSplit==0]=-1

rdmDFclean$highReapSumTopThird = as.numeric(rdmDFclean$reapSpan0sum >=thirdSplitSUM[2]); # top third reap
rdmDFclean$middleReapSumMiddleThird = as.numeric(rdmDFclean$reapSpan0sum > thirdSplitSUM[1] & rdmDFclean$reapSpan0sum <thirdSplitSUM[2])
rdmDFclean$lowReapSumBottomThird = as.numeric(rdmDFclean$reapSpan0sum <=thirdSplitSUM[1]) # bottom third reap

rcsSubLevelLong_clean$highReapSumTertile = as.numeric(rcsSubLevelLong_clean$reapSpan0sum>=thirdSplitSUM[2])
rcsSubLevelLong_clean$lowReapSumTertile = as.numeric(rcsSubLevelLong_clean$reapSpan0sum > thirdSplitSUM[1] & rcsSubLevelLong_clean$reapSpan0sum <thirdSplitSUM[2])
rcsSubLevelLong_clean$modReapSumTertile = as.numeric(rcsSubLevelLong_clean$reapSpan0sum <=thirdSplitSUM[1]) # bottom third reap

rcsSubLevelWide_clean$highReapSumTertile = as.numeric(rcsSubLevelWide_clean$reapSpan0sum>=thirdSplitSUM[2])
rcsSubLevelWide_clean$lowReapSumTertile = as.numeric(rcsSubLevelWide_clean$reapSpan0sum > thirdSplitSUM[1] & rcsSubLevelWide_clean$reapSpan0sum <thirdSplitSUM[2])
rcsSubLevelWide_clean$modReapSumTertile = as.numeric(rcsSubLevelWide_clean$reapSpan0sum <=thirdSplitSUM[1]) # bottom third reap



# reappraisal MEAN scores

medSplitMEAN = median(rcsSubLevelWide_clean$reapSpan0mean, na.rm=T); # median split value
thirdSplitMEAN = quantile(rcsSubLevelWide_clean$reapSpan0mean, probs=c(1/3, 2/3), na.rm=T); # give us lower and upper third quantiles

rdmDFclean$isHighReapMedSplit = as.numeric(rdmDFclean$reapSpan0mean >= medSplitMEAN)
rdmDFclean$isLowReapMedSplit = as.numeric(rdmDFclean$reapSpan0mean < medSplitMEAN)

rdmDFclean$highLowReapMedSplit = rdmDFclean$isHighReapMedSplit
rdmDFclean$highLowReapMedSplit[rdmDFclean$isLowReapMedSplit==0]=-1

rdmDFclean$highReapTopThird = as.numeric(rdmDFclean$reapSpan0mean >=thirdSplitMEAN[2]); # top third reap
rdmDFclean$middleReapMiddleThird = as.numeric(rdmDFclean$reapSpan0mean > thirdSplitMEAN[1] & rdmDFclean$reapSpan0mean <thirdSplitMEAN[2])
rdmDFclean$lowReapBottomThird = as.numeric(rdmDFclean$reapSpan0mean <=thirdSplitMEAN[1]) # bottom third reap

rcsSubLevelLong_clean$highReapTertile = as.numeric(rcsSubLevelLong_clean$reapSpan0mean>=thirdSplitMEAN[2])
rcsSubLevelLong_clean$lowReapTertile = as.numeric(rcsSubLevelLong_clean$reapSpan0mean > thirdSplitMEAN[1] & rcsSubLevelLong_clean$reapSpan0mean <thirdSplitMEAN[2])
rcsSubLevelLong_clean$modReapTertile = as.numeric(rcsSubLevelLong_clean$reapSpan0mean <=thirdSplitMEAN[1]) # bottom third reap

rcsSubLevelWide_clean$highReapTertile = as.numeric(rcsSubLevelWide_clean$reapSpan0mean>=thirdSplitMEAN[2])
rcsSubLevelWide_clean$lowReapTertile = as.numeric(rcsSubLevelWide_clean$reapSpan0mean > thirdSplitMEAN[1] & rcsSubLevelWide_clean$reapSpan0mean <thirdSplitMEAN[2])
rcsSubLevelWide_clean$modReapTertile = as.numeric(rcsSubLevelWide_clean$reapSpan0mean <=thirdSplitMEAN[1]) # bottom third reap

