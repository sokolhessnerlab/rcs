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


def rcsPrimary(subID): # define the function and specify the argument(s)
    
    # let us know things are starting...
    print('starting study for participant', subID)    

    
    #import modules
    import os, time, pandas as pd
    from psychopy import visual

    # Import scripts

    import rcsRDM # risky decision-making task + instructions

    
    # configuration stuff?
    
    # set working directory
    os.chdir("/Users/hayley/Documents/GitHub/rcs/rdmTask")
    #os.chdir("/Users/shlab/Documents/Github/rcs/rdmTask")
    
    # read condition order from pre-existing text file which determines conditions and color for each round of RDM task
    conditionDF = pd.read_csv('rcsConditions.csv')
    
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
    
    

    # set up screen and monitor(s)

    # screensize= [800,800] #how large the screen will be
    # center = [0,0]
    # centerR = [screensize[0]/4,0]
    # centerL = [screensize[0]/-4,0]
    # radius = screensize[0]/5.5
    # rectHeight = radius +2 #rectangle used to cover up half the circle when outcome is gain or loss
    # rectWidth = radius*2+2
    # textHeight = radius/2
    # nT = 5 #for testing purposes

    
    
    # win = visual.Window(
    #     size=screensize,
    #     units="pix",
    #     fullscr=False,
    #     color=[-1, -1, -1] #black screen
    # )
    
    # win.close()

    # reminder of general instructions and practice trials
    
    
    # risky decision-making task
    # input arguments are determined above
    rcsRDM.rcsRDM(subID, cond1, cond2, cond1color, cond2color)

    
     
    
    # cognitive control (working memory) tasks
    
    
    # ospan instructions + instructions quiz + practice + task
    # symspan instructions + instructions quiz + practice + task
    
    # score WM and add to data? or maybe just add this to the analysis script 
    
    # save data
    
    
    
    
