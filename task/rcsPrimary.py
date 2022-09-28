#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 12:20:06 2022

@author: hayley
"""

"""
Primary script for HRB's dissertation project RCS
This script does some set up for the experiment and calls all required scripts to run the risky decision-making and cognitive control tasks
"""


# TO DO:
    #1) FIX SCRIPTS TO SAVE DATA BETTER (BREAKS IF THE TASK STOPS MIDWAY..)
    #2) SET WORKING DIRECTORY BEFORE LOADING EACH MODULE MAYBE THAT WILL WORK BETTER?
    #3) MAKE OSPAN AND SYMSPAN MORE EFFICIENT WHERE WE REPEAT CODE IF TIME
    

def rcsPrimary(subID, isReal): # define the function and specify the argument(s)
    
    # let us know things are starting...
    print('starting study for participant', subID)    

    
    #import modules
    import os
    import pandas as pd
    import sys

    # set working directory
    os.chdir("/Users/shlab/Documents/Github/rcs/task/")

    # add other paths to access scripts
    sys.path.insert(0, '/Users/shlab/Documents/Github/rcs/task/rdmTask')
    sys.path.insert(1, '/Users/shlab/Documents/Github/rcs/task/wmTask/ospan')
    sys.path.insert(2, '/Users/shlab/Documents/Github/rcs/task/wmTask/symspan')    

    
    # Import scripts
    import rcsRDM # risky decision-making task + condition instructions
    import symSpanTask # symspan task
    import ospanTask # ospan task

    
    # read condition order from pre-existing text file which determines conditions and color for each round of RDM task
    conditionDF = pd.read_csv('/Users/shlab/Documents/Github/rcs/task/rdmTask/rcsConditions.csv')
    
    # reading the csv file above does some weird stuff to the subID column, removing the extra characters:
    conditionDF.subID = conditionDF["subID"].str.replace("=","")
    conditionDF.subID = conditionDF["subID"].str.replace('"',"")
    
    # determine condition 1 and condition 2 (0=control, 1 = strategy) for participant
    cond1 = conditionDF.cond1[conditionDF.subID == subID]
    cond1 = cond1.iat[0] # just save the integer, not the extra info like dtype and Name
    cond2 = conditionDF.cond2[conditionDF.subID == subID]
    cond2 = cond2.iat[0] # just save the integer, not the extra info like dtype and Name
     
    # determine the condition colors (green = 0 or purple = 1)
    cond1color = conditionDF.cond1color[conditionDF.subID == subID]
    cond1color = cond1color.iat[0] # just save the integer, not the extra info like dtype and Name
    cond2color = conditionDF.cond2color[conditionDF.subID == subID]
    cond2color = cond2color.iat[0] # just save the integer, not the extra info like dtype and Name
    
    
    # risky decision-making task (input arguments determined above)
    rcsRDM.rcsRDM(subID, cond1, cond2, cond1color, cond2color, isReal)
    
    # ospan instructions + instructions quiz + practice + task
    ospanTask.ospanTask(subID, isReal)
    
    # symspan instructions + instructions quiz + practice + task
    symSpanTask.symSpanTask(subID, isReal)
    
    
    # check that data has been saved...maybe have a back up saving code (if data file does not exists, save it..)

    
    # simple analysis script (checks for missing trials, runs simple glm, scores span tasks, notes whether we keep the data and then adjusts the condition file)
    
    
    
    
    
    
