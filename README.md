## Risky decision-making, context and strategy (RCS) study

- This repository contains scripts and information for setting up and running the task and analysis. 


### 1) Choice set 
 - [Design](./choiceSet)
 - [Parameter Recovery](./parameterRecovery)

### 2) Random assignment
 - [random assignment set up](./task/rcsConditionAssignment.py)
 - [random assignment csv](./task/rcsConditions.csv)

### 3) Task
 - [Primary task script](./task/rcsPrimary.py)
 - [Risky decision-making task script](./task/rcsRDM.py)
 - [Choice set](./task/rcsRDMChoiceSet.py)
 - Working memory task

### 4) Preprocessing
 - Combining data from each participant's RDM and WM
 - Combining data from participants questionnaire responses
 - Quality assurance script
    -  create a note somewhere about exclusion if necessary
    -  output matrix of 0/1 exclusion
 - Data cleaning and set up 
    - imports data exclusion matrix
    - removes participants data where necessary
    - dealing with missed trials from RDM
- Individual-level variables like WM score, ERQ, post-task questionnaires (long and short versions)

### 5) Analysis
- Analysis set up script (e.g. making variables we need for analysis - needs to be R script)
- Analysis script (r markdown script that calls set up script)


