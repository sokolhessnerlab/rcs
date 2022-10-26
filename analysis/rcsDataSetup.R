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


# set up subject ID variables (using dataframe that has exclusion already applied)
subIDchar = unique(rdmDFclean$subID)
nSub = length(subIDchar)
excludeSubID = c("012", "015")


# PUTTING TOGETHER OTHER DATA FILES (OSPAN, SYMSPAN, RDM, POST-ROUND QUESTIONS AND POST-TASK QUESTIONS)
# setting up file paths, loading individual sub files and pulling them together into one and apply exclusion

# RDM post round
rdmFilePath = (file.path(config$path$data$rdmData))
rdmPostQFiles = list.files(rdmFilePath, pattern = "rcsPostQ_sub")

#combine data into 1 file
rdmPostRoundQsdf <- file.path(rdmFilePath,rdmPostQFiles) %>% 
  lapply(read_csv) %>% 
  bind_rows

rdmPostRoundQsdf = rdmPostRoundQsdf[which(!rdmPostRoundQsdf$subID %in% excludeSubID),] # apply exclusion



# Ospan
ospanFilePath = (file.path(config$path$data$ospData))
ospanFiles = list.files(ospanFilePath, pattern = "rcsOSPANbothReal_sub")

ospansubid = regmatches(ospanFiles, regexpr("[0-9][0-9][0-9]", ospanFiles)) # pulls out subid from file names

# combine data into 1 file
ospanDF <- file.path(ospanFilePath,ospanFiles) %>% 
  lapply(read_csv) %>% 
  bind_rows

ospanDF$subID = rep(ospansubid, each = 25); # add subID column


ospanDF = ospanDF[which(!ospanDF$subID %in% excludeSubID),] # apply exclusion


# Symspan
symspanFilePath = (file.path(config$path$data$symspData))
symspanFiles = list.files(symspanFilePath, pattern = "rcsSYMSPANbothReal_sub")

symspansubid = regmatches(symspanFiles, regexpr("[0-9][0-9][0-9]", symspanFiles)) # pulls out subid from file names

# combine data into one file
symspanDF <- file.path(symspanFilePath,symspanFiles) %>% 
  lapply(read_csv) %>% 
  bind_rows

symspanDF$subID = rep(symspansubid, each = 14); # add subID column


symspanDF = symspanDF[which(!symspanDF$subID %in% excludeSubID),] # apply exclusion


# ERQ and Demographic
ERQdemoDF = read_csv(file.path(config$path$directory, 'data/RCS+ERQ+++Demographics_October+20,+2022_16.28.csv'))
ERQdemoDF = ERQdemoDF[which(!ERQdemoDF$subID %in% excludeSubID),] # apply exclusion

# Post-task questionnaires
postTask = read_csv(file.path(config$path$directory, 'data/rcsPostTaskQuestionnaire.csv'))
postTask = postTask[which(!postTask$subID %in% as.numeric(excludeSubID)),] # apply exclusion


# removed missed trials:
nanInd = which(is.na(rdmDFclean$choice));
totNan = length(nanInd); # 84 missed trials 11/11
subNan = unique(rdmDFclean$subID[nanInd]); #(11/11; 24 subs with missed trials)

rdmDFclean = rdmDFclean[which(!is.nan(rdmDFclean$choice)),]; #remove missed trials


# create variables for glmer
rdmDFclean$evLevScaled = rdmDFclean$evLevel/max(rdmDFclean$riskyGain)

# create a variable for condition code
# 1 = control, control
# 2 = control, strategy
# 3 = strategy, control
# 4 = strategy, strategy

conditionsFile = read_csv('/Users/hayley/Documents/GitHub/rcs/task/rdmTask/rcsConditions.csv')

conditionsFile = conditionsFile[1:nSub,]
sum(conditionsFile$condCode==1)
sum(conditionsFile$condCode==2)
sum(conditionsFile$condCode==3)
sum(conditionsFile$condCode==4)

condcode1 = conditionsFile$subID[conditionsFile$condCode==1]
condcode2 = conditionsFile$subID[conditionsFile$condCode==2]
condcode3 = conditionsFile$subID[conditionsFile$condCode==3]
condcode4 = conditionsFile$subID[conditionsFile$condCode==4]

# pgamble diff between round 1 and 2 
# control, control
mean(RDMqualityCheck$pgambleRound1[RDMqualityCheck$subID %in% as.numeric(condcode1)] -RDMqualityCheck$pgambleRound2[RDMqualityCheck$subID %in% as.numeric(condcode1)])

# control, strategy
mean(RDMqualityCheck$pgambleRound1[RDMqualityCheck$subID %in% as.numeric(condcode2)] -RDMqualityCheck$pgambleRound2[RDMqualityCheck$subID %in% as.numeric(condcode2)])

# strategy, control
mean(RDMqualityCheck$pgambleRound1[RDMqualityCheck$subID %in% as.numeric(condcode3)] -RDMqualityCheck$pgambleRound2[RDMqualityCheck$subID %in% as.numeric(condcode3)])

# strategy, strategy
mean(RDMqualityCheck$pgambleRound1[RDMqualityCheck$subID %in% as.numeric(condcode4)] -RDMqualityCheck$pgambleRound2[RDMqualityCheck$subID %in% as.numeric(condcode4)])



scaleby = max(rdmDFclean$riskyGain, na.rm=T)
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


# Calculate cumulative earnings (within each phase) for each participant and scale trial so that it is 0-1 for each participant
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


rdmDFclean$earninngs = earningsByRound;
rdmDFclean$earningsSC = earningsByRoundScaled;
rdmDFclean$trialSC = trialByRound;


# quick summary about cumulative earnings:
# phase 1: range = $1576 - $2467, median = $2087, mean = $2080
# phase 2: range = $1597 - $2492, median = $2135, mean = $2133



# recode strategy
rdmDFclean$strategy01 = rdmDFclean$strategy
rdmDFclean$strategy01[rdmDFclean$strategy01==1] =-1
rdmDFclean$strategy01[rdmDFclean$strategy01==2] =1


rdmDFclean$subIDnum = as.numeric(rdmDFclean$subID)


rdmDFclean$round01 = rdmDFclean$roundRDM
rdmDFclean$round01[rdmDFclean$round01 == 1] = 0
rdmDFclean$round01[rdmDFclean$round01 == 2] = 1
