#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 09:18:44 2022

@author: shlab
"""

"""
symmetry span task for HRB dissertation project: Risk, context and strategy.

For this study, we are running the shortened version (Foster et al 2014) of both the operation span and symmetry span tasks.
We are doing one block for each. 

The structure of the complex span tasks are very similar: instructions, practice letters/red square only, practice distractors only, the practice both.
 
"""
    
subID = '001'


# Import modules we need
import os, random, time
import pandas as pd
import numpy as np
from psychopy import visual, core, event, monitors
import statistics
#import numpy as np


#change directory
os.chdir('/Users/shlab/Documents/GitHub/rcs/wmTask/symspan')



#load stimuli

# set up screen parameters
# Screen dimensions and drawing stuff
#scrnsize= [800,800] #how large the screen will be
#scrnsize=[1280,1024] # CORRECT DIMENSIONS FOR REAL TASK
scrnsize = [1024,819.2] # 80% of correct size for mac laptop
center = [0,100]
centerR = [scrnsize[0]/4,100]
centerL = [scrnsize[0]/-4,100]
radius = scrnsize[0]/5.5
rectHeight = radius +2 #rectangle used to cover up half the circle when outcome is gain or loss
rectWidth = radius*2+2
#textHeight = radius/2.1
textHeight = 40
wrap = scrnsize[0]*.9 # text wrapping
boxLetterSize = 90; # letter box size for recall screen
matrixBoxSize = 115


# Set up the window
win = visual.Window(
    size=scrnsize,
    units="pix",
    fullscr=False,
    color=[-1, -1, -1], #black screen
    screen=1 # on second screen
)


# set up stimuli

## INSTRUCTIONS STIMULI
generalInstructionsPg1 = visual.TextStim(
    win,
    text= "In this experiment you will try to memorize the position of colored squares you see on the screen while you also make judgments about other pictures. \n\nIn the next few minutes, you will have some practice to get you familiar with how the experiment works. \n\nWe will begin by practicing the 'square' part of the experiment. \n\n\nPress 'enter' to continue.",
    pos = center,
    color="white",
    height = textHeight, 
    wrapWidth=wrap,
    alignText="left"
)

generalInstructionsPg2 = visual.TextStim(
    win,
    text = "For this practice set, squares will appear on the screen one at a time. \n\nTry to remember where each square was, in the order it was presented in. \n\nAfter 2 - 5 squares have been shown, you will see a grid of the 16 possible places the squares could have been. \n\nYour job is to select each square in the order presented. \n\nTo do this, use the mouse to select the appropriate boxes. \n\nThe squares you select will turn red.\n\n\nPress 'enter' to continue.",
    pos = center,
    color="white",
    height = textHeight,
    wrapWidth=wrap,
    alignText="left"
)

generalInstructionsPg3 = visual.TextStim(
    win,
    text = "When you have selected all the squares, and they are in the correct order, hit the ENTER box at the bottom right of the screen. \n\nIf you make a mistake, hit the CLEAR box to start over. \n\nIf you forget one of the squares, click the BLANK box to mark the spot for the missing square. \n\nRemember, it is very important to get the squares in the same order as you see them. \n\nIf you forget one, use the BLANK box to mark the position. \n\nPlease ask the experimenter any questions you may have at this time. \n\n\nWhen you are ready, press 'enter' to start the square practice.",
    pos = center,
    color="white",
    height = textHeight,
    wrapWidth=wrap,
    alignText="left"
)


# red square stimuli (with matrix for response)
# define location for each column of the recall matrix  
COL1horiz = scrnsize[0]*-.4
COL2horiz = scrnsize[0]*-.28
COL3horiz = scrnsize[0]*-.16
COL4horiz = scrnsize[0]*-.04
ROW1vert = scrnsize[1]*.27
ROW2vert = scrnsize[1]*.12
ROW3vert = scrnsize[1]*-.03
ROW4vert = scrnsize[1]*-.18



box_r1c1 = visual.Rect(
    win, 
    name='1',
    width=matrixBoxSize, 
    height=matrixBoxSize, 
    units='pix', 
    pos=[COL1horiz,ROW1vert], 
    fillColor="white" #white
)


box_r1c2 = visual.Rect(
    win, 
    name='2',
    width=matrixBoxSize, 
    height=matrixBoxSize, 
    units='pix', 
    pos=[COL2horiz, ROW1vert], 
    fillColor=[1,1,1] #white
)

box_r1c3 = visual.Rect(
    win, 
    name='3',
    width=matrixBoxSize, 
    height=matrixBoxSize, 
    units='pix', 
    pos=[COL3horiz, ROW1vert], 
    fillColor=[1,1,1] #white
)

box_r1c4 = visual.Rect(
    win, 
    name='4',
    width=matrixBoxSize, 
    height=matrixBoxSize, 
    units='pix', 
    pos=[COL4horiz, ROW1vert], 
    fillColor=[1,1,1] #white
)



box_r2c1 = visual.Rect(
    win, 
    name='5',
    width=matrixBoxSize, 
    height=matrixBoxSize, 
    units='pix', 
    pos=[COL1horiz,ROW2vert], 
    fillColor="white" #white
)

box_r2c2 = visual.Rect(
    win, 
    name='6',
    width=matrixBoxSize, 
    height=matrixBoxSize, 
    units='pix', 
    pos=[COL2horiz,ROW2vert], 
    fillColor="white" #white
)

box_r2c3 = visual.Rect(
    win, 
    name='7',
    width=matrixBoxSize, 
    height=matrixBoxSize, 
    units='pix', 
    pos=[COL3horiz,ROW2vert], 
    fillColor="white" #white
)

box_r2c4 = visual.Rect(
    win, 
    name='8',
    width=matrixBoxSize, 
    height=matrixBoxSize, 
    units='pix', 
    pos=[COL4horiz,ROW2vert], 
    fillColor="white" #white
)

box_r3c1 = visual.Rect(
    win, 
    name='9',
    width=matrixBoxSize, 
    height=matrixBoxSize, 
    units='pix', 
    pos=[COL1horiz,ROW3vert], 
    fillColor="white" #white
)

box_r3c2 = visual.Rect(
    win, 
    name='10',
    width=matrixBoxSize, 
    height=matrixBoxSize, 
    units='pix', 
    pos=[COL2horiz,ROW3vert], 
    fillColor="white" #white
)

box_r3c3 = visual.Rect(
    win, 
    name='11',
    width=matrixBoxSize, 
    height=matrixBoxSize, 
    units='pix', 
    pos=[COL3horiz,ROW3vert], 
    fillColor="white" #white
)

box_r3c4 = visual.Rect(
    win, 
    name='12',
    width=matrixBoxSize, 
    height=matrixBoxSize, 
    units='pix', 
    pos=[COL4horiz,ROW3vert], 
    fillColor="white" #white
)

box_r4c1 = visual.Rect(
    win, 
    name='13',
    width=matrixBoxSize, 
    height=matrixBoxSize, 
    units='pix', 
    pos=[COL1horiz,ROW4vert], 
    fillColor="white" #white
)

box_r4c2 = visual.Rect(
    win, 
    name='14',
    width=matrixBoxSize, 
    height=matrixBoxSize, 
    units='pix', 
    pos=[COL2horiz,ROW4vert], 
    fillColor="white" #white
)

box_r4c3 = visual.Rect(
    win, 
    name='15',
    width=matrixBoxSize, 
    height=matrixBoxSize, 
    units='pix', 
    pos=[COL3horiz,ROW4vert], 
    fillColor="white" #white
)

box_r4c4 = visual.Rect(
    win, 
    name='16',
    width=matrixBoxSize, 
    height=matrixBoxSize, 
    units='pix', 
    pos=[COL4horiz,ROW4vert], 
    fillColor="white" #white
)


blankButton = visual.TextStim(
    win, 
    text='BLANK', 
    pos = [scrnsize[0]*.3,scrnsize[1]*.25],
    color="black", 
    height=70
)

blankButtonBox = visual.Rect(
    win, 
    name='*',
    width=boxLetterSize*3, 
    height=boxLetterSize*1.5, 
    units='pix', 
    pos=blankButton.pos, 
    fillColor=[1,1,1] #white
)


clearButton = visual.TextStim(
    win, 
    text='CLEAR', 
    pos = [scrnsize[0]*.3,scrnsize[1]*.025],
    color="black", 
    height=70
)

clearButtonBox = visual.Rect(
    win, 
    width=boxLetterSize*3, 
    height=boxLetterSize*1.5, 
    units='pix', 
    pos=clearButton.pos, 
    fillColor="red" #white
)


enterButton = visual.TextStim(
    win, 
    text='ENTER', 
    pos = [scrnsize[0]*.3,scrnsize[1]*-.2],
    color="black", 
    height=70
)

enterButtonBox = visual.Rect(
    win, 
    width=boxLetterSize*3, 
    height=boxLetterSize*1.5, 
    units='pix', 
    pos=enterButton.pos, 
    fillColor=[0,.6,0] #white
)

# symmetry ratings
# general stimlui

blankScreen = visual.TextStim(
    win,
    pos = [0,0],
    color="white",
    height=textHeight,
    text=" "
)

fixationScreen = visual.TextStim(
    win,
    pos = [0,0],
    color="white",
    height=textHeight,
    text="+"
)


# Do red square practice noly
    # 4 trials with set sizes {2,2,3,3}, uses images to show red square matrices
box_r1c1.draw()
box_r1c2.draw()
box_r1c3.draw()
box_r1c4.draw()
box_r2c1.draw()
box_r2c2.draw()
box_r2c3.draw()
box_r2c4.draw()
box_r3c1.draw()
box_r3c2.draw()
box_r3c3.draw()
box_r3c4.draw()
box_r4c1.draw()
box_r4c2.draw()
box_r4c3.draw()
box_r4c4.draw()

blankButtonBox.draw()
blankButton.draw()
clearButtonBox.draw()
clearButton.draw()
enterButtonBox.draw()
enterButton.draw()

win.flip()
core.wait(2)
win.close()
    
# Do symmetry ratings only
    # 15 trials where participants report whether the images are symmetrical (using true or false, like the ospan)
# Red square - symmetry practice
    # 3 trials with set size = 2
# Red square - symmetry real
    # 4 trials with set sizes  2- 5
# save data
