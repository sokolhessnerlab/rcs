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

#another
test for github


def rcsPrimary(subID): # define the function and specify the argument(s)
    
    # let us know things are starting...
    print('starting study for participant', subID)    

    
    #import modules
    import os, time, pandas as pd
    from psychopy import visual

    # Import scripts

    # import rcsRDM 
    
    # configuration stuff?
    
    # set working directory
    #os.chdir("/Users/hayley/Documents/GitHub/rcs/task")
    os.chdir("/Users/shlab/Documents/Github/rcs/task")
    
    # read condition order from pre-existing text file

    conditionDF = pd.read_csv('rcsConditions.csv')
    
    # reading the csv file above does some weird stuff to the subID column, removing the extra characters:
    conditionDF.subID = conditionDF["subID"].str.replace("=","")
    conditionDF.subID = conditionDF["subID"].str.replace('"',"")
    
    # save condition 1 and condition 2 (0=control, 1 = strategy) for participant
    cond1 = conditionDF.cond1[conditionDF.subID == subID]
    cond2 = conditionDF.cond1[conditionDF.subID == subID]
     
       
    # set up data structure, filename, etc
    #

    # datetime = time.strftime("%Y%m%d-%H%M%S"); # save date and time
    # filename = "condition_" + "sub" + subID + "_" + datetime + ".csv"; # make filename
    
    # condData = {
    #   "subID": subID,
    #   "cond1": int(cond1),
    #   "cond2": int(cond2)
    # }
    

    # set up screen and monitor(s)

    screensize= [800,800] #how large the screen will be
    center = [0,0]
    centerR = [screensize[0]/4,0]
    centerL = [screensize[0]/-4,0]
    radius = screensize[0]/5.5
    rectHeight = radius +2 #rectangle used to cover up half the circle when outcome is gain or loss
    rectWidth = radius*2+2
    textHeight = radius/2
    nT = 5 #for testing purposes

    
    
    win = visual.Window(
        size=screensize,
        units="pix",
        fullscr=False,
        color=[-1, -1, -1] #black screen
    )
    
    win.close()

    # reminder of general instructions and practice trials
    
    
    # risky decision-making task round 1
    # change rdm task to take cond1 and cond2 as argument along with subID
    
    # anything we want to do before the second round that is not covered by RDM task
        # save risky decision-making data (this will already be saved by the RDM task but perhaps we want to set it up so it can be easily combined with round 2)
    
    
    # risky decision-making task round 2
    
    
    # randomly select between the two outcomes in the risky decision-making tasks and display on screen and save that information
    
    
    # cognitive control (working memory) tasks
    
    
    # ospan instructions + instructions quiz + practice + task
    # symspan instructions + instructions quiz + practice + task
    
    # score WM and add to data? or maybe just add this to the analysis script 
    
    # save data
    
    
    
    
