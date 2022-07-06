#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 16:06:44 2022

@author: hayley
"""

"""
Complex span tasks for HRB dissertation project: Risk, context and strategy.

For this study, we are running the shortened version (Foster et al 2014) of both the operation span and symmetry span tasks.
We are doing one block for each. 

The structure of the complex span tasks are very similar: instructions, practice letters/red square only, practice distractors only, the practice both.
 
"""
    
# Import modules we need
import random, time, os
import pandas as pd
from psychopy import visual, core, event, monitors
import numpy as np

# change directory
os.chdir('/Users/hayley/Documents/Github/rcs/wmTask') # hb mac


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


# Set up the window
win = visual.Window(
    size=scrnsize,
    units="pix",
    fullscr=False,
    color=[-1, -1, -1], #black screen
    screen=1 # on second screen
)


## INSTRUCTIONS STIMULI

## LETTER STIMULI

# grid of letters for participants to respond
# Row 1: F, H, J 
# Row 2: K, L, N 
# Row 3: P, Q, R 
# Row 4: S, T, Y

# define location for each column of the letter grid 
COL1horiz = scrnsize[0]*-.35
COL2horiz = scrnsize[0]*-.15
COL3horiz = scrnsize[0]*.05
ROW1vert = scrnsize[1]*.4
ROW2vert = scrnsize[1]*.2
ROW3vert = 0
ROW4vert = scrnsize[1]*-.2

boxLetterSize = 90;

F_r1c1 = visual.TextStim(
    win, 
    text='F', 
    pos = [COL1horiz,ROW1vert],
    color="black", 
    height=boxLetterSize
)

Fbox = visual.Rect(
    win, 
    width=boxLetterSize, 
    height=boxLetterSize, 
    units='pix', 
    pos=[COL1horiz,ROW1vert], 
    fillColor=[1,1,1] #white
)

H_r1c2 = visual.TextStim(
    win, 
    text='H', 
    pos = [COL2horiz,ROW1vert],
    color="black", 
    height=boxLetterSize
)

Hbox = visual.Rect(
    win, 
    width=boxLetterSize, 
    height=boxLetterSize, 
    units='pix', 
    pos=H_r1c2.pos, 
    fillColor=[1,1,1] #white
)

J_r1c3 = visual.TextStim(
    win, 
    text='J', 
    pos = [COL3horiz,ROW1vert],
    color="black", 
    height=boxLetterSize
)

Jbox = visual.Rect(
    win, 
    width=boxLetterSize, 
    height=boxLetterSize, 
    units='pix', 
    pos=J_r1c3.pos, 
    fillColor=[1,1,1] #white
)


K_r2c1 = visual.TextStim(
    win, 
    text='K', 
    pos = [COL1horiz,ROW2vert],
    color="black", 
    height=boxLetterSize
)

Kbox = visual.Rect(
    win, 
    width=boxLetterSize, 
    height=boxLetterSize, 
    units='pix', 
    pos=K_r2c1.pos, 
    fillColor=[1,1,1] #white
)


L_r2c2 = visual.TextStim(
    win, 
    text='L', 
    pos = [COL2horiz,ROW2vert],
    color="black", 
    height=boxLetterSize
)

Lbox = visual.Rect(
    win, 
    width=boxLetterSize, 
    height=boxLetterSize, 
    units='pix', 
    pos=L_r2c2.pos, 
    fillColor=[1,1,1] #white
)


N_r2c3 = visual.TextStim(
    win, 
    text='N', 
    pos = [COL3horiz,ROW2vert],
    color="black", 
    height=boxLetterSize
)

Nbox = visual.Rect(
    win, 
    width=boxLetterSize, 
    height=boxLetterSize, 
    units='pix', 
    pos=N_r2c3.pos, 
    fillColor=[1,1,1] #white
)

P_r3c1 = visual.TextStim(
    win, 
    text='P', 
    pos = [COL1horiz,ROW3vert],
    color="black", 
    height=boxLetterSize
)

Pbox = visual.Rect(
    win, 
    width=boxLetterSize, 
    height=boxLetterSize, 
    units='pix', 
    pos=P_r3c1.pos, 
    fillColor=[1,1,1] #white
)


Q_r3c2 = visual.TextStim(
    win, 
    text='Q', 
    pos = [COL2horiz,ROW3vert],
    color="black", 
    height=boxLetterSize
)

Qbox = visual.Rect(
    win, 
    width=boxLetterSize, 
    height=boxLetterSize, 
    units='pix', 
    pos=Q_r3c2.pos, 
    fillColor=[1,1,1] #white
)

R_r3c3 = visual.TextStim(
    win, 
    text='R', 
    pos = [COL3horiz,ROW3vert],
    color="black", 
    height=boxLetterSize
)

Rbox = visual.Rect(
    win, 
    width=boxLetterSize, 
    height=boxLetterSize, 
    units='pix', 
    pos=R_r3c3.pos, 
    fillColor=[1,1,1] #white
)

S_r4c1 = visual.TextStim(
    win, 
    text='S', 
    pos = [COL1horiz,ROW4vert],
    color="black", 
    height=boxLetterSize
)

Sbox = visual.Rect(
    win, 
    width=boxLetterSize, 
    height=boxLetterSize, 
    units='pix', 
    pos=S_r4c1.pos, 
    fillColor=[1,1,1] #white
)

T_r4c2 = visual.TextStim(
    win, 
    text='T', 
    pos = [COL2horiz,ROW4vert],
    color="black", 
    height=boxLetterSize
)

Tbox = visual.Rect(
    win, 
    width=boxLetterSize, 
    height=boxLetterSize, 
    units='pix', 
    pos=T_r4c2.pos, 
    fillColor=[1,1,1] #white
)

Y_r4c3 = visual.TextStim(
    win, 
    text='Y', 
    pos = [COL3horiz,ROW4vert],
    color="black", 
    height=boxLetterSize
)

Ybox = visual.Rect(
    win, 
    width=boxLetterSize, 
    height=boxLetterSize, 
    units='pix', 
    pos=Y_r4c3.pos, 
    fillColor=[1,1,1] #white
)

blankButton = visual.TextStim(
    win, 
    text='BLANK', 
    pos = [scrnsize[0]*.3,scrnsize[1]*.37],
    color="black", 
    height=70
)

blankButtonBox = visual.Rect(
    win, 
    width=boxLetterSize*3, 
    height=boxLetterSize*1.5, 
    units='pix', 
    pos=blankButton.pos, 
    fillColor=[1,1,1] #white
)


clearButton = visual.TextStim(
    win, 
    text='CLEAR', 
    pos = [scrnsize[0]*.3,scrnsize[1]*.1],
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
    pos = [scrnsize[0]*.3,scrnsize[1]*-.17],
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

# draw the stimuli for the letter grid
Fbox.draw()
Hbox.draw()
Jbox.draw()
Kbox.draw()
Lbox.draw()
Nbox.draw()
Pbox.draw()
Qbox.draw()
Rbox.draw()
Sbox.draw()
Tbox.draw()
Ybox.draw()
blankButtonBox.draw()
clearButtonBox.draw()
enterButtonBox.draw()
F_r1c1.draw()
H_r1c2.draw()
J_r1c3.draw()
K_r2c1.draw()
L_r2c2.draw()
N_r2c3.draw()
P_r3c1.draw()
Q_r3c2.draw()
R_r3c3.draw()
S_r4c1.draw()
T_r4c2.draw()
Y_r4c3.draw()
blankButton.draw()
clearButton.draw()
enterButton.draw()

win.flip()
core.wait(3)
win.close()


# NEXT STEP - RECORD LETTER MOUSE RESPONSE AND SHOW RESPONSE ON SCREEN

## OPERATION STIMULI


