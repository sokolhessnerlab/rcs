# Data and analysis documentation for RCS

## Data Files

All data files are stored on the S drive

#### 1. rdmData (directory)

Each participant has 6 rdm files:

1.  practice trials
2.  real trials both rounds
3.  responses to post task questions (2 per round)
4.  choice set from round 1
5.  choice set from round 2
6.  selected outcomes (including the final one for payment)

#### 2. ospanData

Each participant has 4 ospan files:

1.  letter practice
2.  math practice
3.  letter/math practice
4.  letter/math real

Note that these files don't save the sub ID inside the file but is included in the file name.

#### 3. symspanData

Each participant has 4 ospan files:

1.  matrix practice
2.  symmetry practice
3.  matrix/symmetry practice
4.  matrix/symmetry real

Note that these files don't save the sub ID inside the file but is included in the file name.

#### 4. Post-task questionnaire 

-   one file for all participants

#### 5. Emotion regulation + demographic questionnaires

-   one file for all participants

#### 6. Rdata Files (these are outputs from analysis scripts)

-   rdmQualityCheck.Rdata

-   ERQscores.Rdata

-   complexSpanScores.Rdata

-   ospan_clean.Rdata

-   rdmDF_clean.Rdata

-   symspan_clean.Rdata

-   subLevelwide.Rdata (not created yet - combines single scores for anything possible in our study)

-   subLevellong.Rdata (not created yet - combines single scores for anything possible in our study)

-   complexSpanExclude.Rdata

    -   1 = exclude, 0 = keep

-   rdmExclude.Rdata

    -   1 = exclude, 0 = keep

-   ERQexclude.Rdata

    -   1 = exclude, 0 = keep

-   allExclusion.Rdata (not created yet)

#### 7. CombinedData

-   empty as of now

## Scripts

1.  rcsDataQA.Rmd
    -   Loads individual level data (rdm, ospan, symspan, erq and post task questionnaires)

    -   combines individual participant data into one Rdata file

    -   check exclusion criteria for rdm, ospan, symspan, and ERQ data and saves that information as Rdata

    -   
2.  rcsDataSetup.R
3.  rcsBasicAnalysis.Rmd
