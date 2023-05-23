# Analysis scripts and data documentation for RCS

## Scripts

1.  rcsDataQA.Rmd
    -   Loads individual level raw data (rdm, ospan, symspan, erq and post task questionnaires)
    -   combines individual participant data into indivivdual Rdata files (one for each task/questionnaire)
    -   does some basic checks (e.g. missed trials, pgamble over all, reaction time)
    -   checks and applies exclusion criteria for rdm, ospan, symspan, and ERQ data and saves that information as Rdata files
    -   scores ospan, symspan and ERQ
    -   creates big exclusion matrix for all tasks (e.g. which task(s), if any, is each participant excluded from?)
    -   cleans up/recodes demographic responses
    -   combines ALL data into a single Rdata frame
    -   makes subject-level dataframes - wide and long formats
    -   several outputs from this script (most, if not all, of the Rdata listed below is generated from this script)

        -  round1passfail.Rdata: indicates whether each participant passed each inclusion criteria in round 1 of RDM task
        - round2passfail.Rdata: indicates whether each participant passed each inclusion criteria in round 2 of RDM task
        - rdmExclude.Rdata: indicates whether participant will be excluded (based on missing more than 2 inclusion check points)
        - rdmQualityCheck.Rdata: a massive matrix with information about data quality for each participant (e.g. missed trial, pgam, glm results, etc)
        - rdmDFall.Rdata: includes all RDM data + ospan, symspan, ERQ, demographic, post round Qs, post-task questionnaires (the numeric ones) 
        - rdmDFall_clean.Rdata: same as above but exclusions across the tasks are applied
        - rcsSubLevelLong.Rdata: individual level dataframe long format where each participant has two rows for each round (includes all participants)
        - rcsSubLevelLongClean.Rdata: same as above but RDM exclusion applied
        - rcsSubLevelWide.Rdata individual level dataframe wide format where each participant has one row (includes all participants)
        - rcsSubLevelWideClean.Rdata same as above but RDM exclusion applied
        - rdmOutcomes.Rdata: dataframe where each participants has a row with outcomes selected after each round and for payment at the end
        - rdmPostRoundQs.Rdata: dataframe where each participant has a row with their responses to the post round questions
        - postTaskNumericOnly.Rdata: numeric responses on post task questionnaire for each participant (e.g. does not include text responses)
        - demographic.Rdata: recoded demographic data (e.g. numeric codes for race, ethnicity, gender)
        - rcsAllExclusion.Rdata: big exclusion matrix that indicates whether the participant is excluded from any of the tasks/questionnaires
        - ERQscores.Rdata: emotion regulation questionnaire scores
        - ERQexclude.Rdata: matrix that indicates whether participant is excluded from ERQ (e.g. missing responses)
        - complexSpanScores.Rdata: scores for ospan and symspan
        - complexSpanExclusion.Rdata: exclusions for ospan and symspan
        - symspan_clean.Rdata: sym span dataframe with sym span exclusion applied
        - ospan_clean.Rdata: ospan dataframe with ospan exclusion applied



2.  rcsDataSetup.R
    -   This script creates the variables we need for glmer and other analysis (e.g. past outcome variable).
    
3.  rcsBasicAnalysis.Rmd
    - basic analysis including averages, correlations, glmer models

## Data Files

All data files are stored on the S drive. Copy of raw data files are located on [OSF](https://osf.io/2wb5z/) as well.

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

    -   several columns that were used to judge quality in each RDM round including pgamble, glm, total/total missed/proportion missed for two types of attention checks, missed trials, reaction time.

-   ERQscores.Rdata

    -   includes sub ID, reappraisal score, and suppression score

-   complexSpanScores.Rdata

    -   includes sub ID, ospan score and symspan score

-   ospan_clean.Rdata

    -   removed participants who scored less than 85% on math

-   symspan_clean.Rdata

    -   removed participants who scored less than 85% on symmetry judgmenets

-   complexSpanExclude.Rdata

    -   1 = exclude, 0 = keep

-   round1passfail.Rdata

    -   includes columns: subID, missT, missACs, pgamble, glm, rt, total

    -   1 = pass, 0 = fail.

    -   total can range from 0 (meaning failed all criteria) to 5 (meaning passed all criteria)

-   round2passfail.Rdata

    -   same as above in round1passfail.Rdata

-   rdmExclude.Rdata

    -   includes subID, round 1 exclude, round 2 exclude, overall exclude

    -   based on total counts from round1passfail and round2passfail where participants had to score 4-5 in BOTH rounds to be included.

    -   1 = exclude, 0 = keep

-   ERQexclude.Rdata

    -   1 = exclude, 0 = keep

-   rcsAllExclusion.Rdata

    -   combines rdm round 1 and 2 and overall, ERQ, ospan and symspan exclusion

    -   1 = exclude, 0 = keep

-   demographic.Rdata

    -   includes race, ethnicity, gender and age information (along with codes for each)

-   Post round Qs (instruction difficulty and how often ratings)

    -   includes condition code (1 = nat/nat, 2 = nat/strat, 3 = strat/nat, 4 = strat,nat

-   postTaskNumericOnly.Rdata

    -   Just include numeric data (not text responses)

-   rdmOutcomes.Rdata

    -   4 column dataframe that includes a row for each participants with selected outcome in round 1 and round 2, selected outcome for payment and 1/2 of that amount

-   rdmDFall.Rdata

    -   48 columns including RDM data, ospan score, symspan score, ERQ scores, demographic info, post-round and post-task questions (numeric responses only), and selected outcomes/payment in rdm

    -   the number of rows in this dataframe should always be nTrials(131) x rounds(2) x nSub

-   rdmDFall_clean.Rdata

    -   cleaned up version of dataframe above including removing subs excluded from RDM, removing missed RDM trials and for NAs in variables for participants included in RDM but failed other variable criterias (e.g. ospan math correct was less than 85%).

    -   this dataframe should always have less rows than the one above.

-   subLevelWide.Rdata

    -   Individual-level dataframe where each row is a participant

-   subLevelWideClean.Rdata

    -   Exclusion (rdm, complex span, and ERQ) applied to the individual-level (wide) dataframe

-   subLevelLong.Rdata

    -   Individual-level dataframe where each participant has two rows, one for each round

-   subLevelLongClean.Rdata

    -   Exclusion applied to the individual-level (long) dataframe

#### 7. CombinedData

-   empty as of now - is intended for any of the combined data frames above that need to be exported as CSV or other non-Rdata formats.

#### 8. Raw data for OSF (on both OSF and lab drive)
6 files that include raw data for ALL participants (n=134; exclusion not applied, no scoring included):
    1. Risky decision-making data from both rounds
    2. Post round questionnaires (RDM)
    3. RDM outcome information
    4. Post task questions
    5. Symspan
    6. Ospan
    7. ERQ + demographic 

