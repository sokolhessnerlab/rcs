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
ERQdemoDF = read_csv(file.path(config$path$directory, 'data/RCS+ERQ+++Demographics_October+19,+2022_16.32.csv'))
ERQdemoDF = ERQdemoDF[which(!ERQdemoDF$subID %in% excludeSubID),] # apply exclusion

# Post-task questionnaires
postTask = read_csv(file.path(config$path$directory, 'data/rcsPostTaskQuestionnaire.csv'))
postTask = postTask[which(!postTask$subID %in% as.numeric(excludeSubID)),] # apply exclusion


# removed missed trials:



