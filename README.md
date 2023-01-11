## Risky decision-making, context and strategy (RCS) study

- This repository contains scripts and information for setting up and running the task and analysis. 


### 1) Choice set design
 - [Choice set script in R](./choiceSet/rcsChoiceSet.R) and [example choice set plots](./choiceSet/exampleChoiceSet.pdf)
 - [Parameter Recovery + results](./parameterRecovery)


### 2) [Task](./task/)
This study is run using a primary script that references the individual tasks (risky decision-making, operation span, symmetry span) scripts.
 - [Primary task script](./task/rcsPrimary.py)
 - [Risky decision-making task directory](./task/rdmTask/)
 - [Operation span task directory](./task/ospan)
 - [Symmetry span task directory](./task/symspan)

### 3) [Preprocessing/Analysis](./analysis)
- Preprocessing or QA is done with [rcsDataQA.Rmd](./analysis/rcsDataQA.Rmd). 
- Data set up is done with [rcsDataSetup.R](./analysis/rcsDataSetup.R) (i.e. getting data in format we can work with).
- Basic analyses (e.g. calculating means, looking at correlations and linear mixed effects regressions) is done with [rcsBasicAnalysis.Rmd](./analysis/rcsBasicAnalysis.Rmd).
- Modeling scripts (forthcoming...)

For more details on these scripts and THE DATA, go to this [README.md](./analysis/README.md)



