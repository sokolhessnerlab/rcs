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
import os, random
#import pandas as pd
from psychopy import visual, core, event, monitors
#import numpy as np

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
boxLetterSize = 90; # letter box size for recall screen


# Set up the window
win = visual.Window(
    size=scrnsize,
    units="pix",
    fullscr=False,
    color=[-1, -1, -1], #black screen
    screen=1 # on second screen
)


## INSTRUCTIONS STIMULI
generalInstructionsPg1 = visual.TextStim(
    win,
    text= "In this experiment you will try to memorize letters you see on the screen while you also solve simple math problems. \n\nIn the next few minutes, you will have some practice to get you familiar with how the experiment works. \n\nWe will begin by practicing the letter part of the experiment. \n\n\nClick 'enter' to continue.",
    pos = center,
    color="white",
    height = textHeight, 
    wrapWidth=wrap,
    alignText="left"
)

generalInstructionsPg2 = visual.TextStim(
    win,
    text= "For this practice set, letters will appear on the screen one at a time. \n\nTry to remember each letter in the order presented. \n\nAfter 2-3 letters have been shown, you will see a screen listing 12 possible letters. \n\nYour job is to select each letter in the order presented. \n\nTo do this, use the mouse to select the box for each letter. \n\nThe letters you select will appear at the bottom of the screen. \n\n\nClick 'enter' to continue.",
    pos = center,
    color="white",
    height = textHeight,
    wrapWidth=wrap,
    alignText="left"
)

generalInstructionsPg3 = visual.TextStim(
    win,
    text = "When you have selected all the letters, and they are in the correct order, hit the ENTER box at the bottom right of the screen. \n\nIf you make a mistake, hit the CLEAR box to start over. \n\nIf you forget one of the letters, click the BLANK box to mark the spot for the missing letter. \n\nRemember, it is very important to get the letters in the same order as you see them. \n\nIf you forget one, use the BLANK box to mark the position. \n\nPlease ask the experimenter any questions you may have at this time. \n\n\nWhen you're ready, click enter to start the letter practice.",
    pos = center,
    color="white",
    height = textHeight,
    wrapWidth=wrap,
    alignText="left"
)



## LETTER STIMULI


letterList = ["F", "H", "J", "K", "L", "N", "P", "Q", "R", "S", "T", "Y"]

letterDisplay = visual.TextStim(
    win,
    pos = [0,0],
    color="white",
    height=boxLetterSize
)


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


# grid of letters for participants to respond
# Row 1: F, H, J 
# Row 2: K, L, N 
# Row 3: P, Q, R 
# Row 4: S, T, Y

# define location for each column of the letter grid 
COL1horiz = scrnsize[0]*-.35
COL2horiz = scrnsize[0]*-.15
COL3horiz = scrnsize[0]*.05
ROW1vert = scrnsize[1]*.27
ROW2vert = scrnsize[1]*.1
ROW3vert = scrnsize[1]*-.07
ROW4vert = scrnsize[1]*-.24



F_r1c1 = visual.TextStim(
    win, 
    text='F', 
    pos = [COL1horiz,ROW1vert],
    color="black", 
    height=boxLetterSize
)

Fbox = visual.Rect(
    win, 
    name='F',
    width=boxLetterSize, 
    height=boxLetterSize, 
    units='pix', 
    pos=[COL1horiz,ROW1vert], 
    fillColor="white" #white
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
    name='H',
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
    name='J',
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
    name='K',
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
    name = 'L',
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
    name='N',
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
    name='P',
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
    name='Q',
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
    name='R',
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
    name='S',
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
    name='T',
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
    name='Y',
    width=boxLetterSize, 
    height=boxLetterSize, 
    units='pix', 
    pos=Y_r4c3.pos, 
    fillColor=[1,1,1] #white
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


showLetterResponse = visual.TextStim(
    win, 
    pos = [COL1horiz +100, ROW4vert -100],
    color="blue", 
    height=boxLetterSize,
)


letterPracticeRecallText = visual.TextStim(
    win,
    pos = [0,scrnsize[1]*.4],
    color="white",
    height=textHeight,
    text="Select the letters in the order presented. \nUse the blank button to fill in forgotten letters.",
    wrapWidth=wrap
)

letterFeedbackText = visual.TextStim(
    win,
    pos = [0,0],
    color="white",
    height = textHeight,
    wrapWidth = wrap
)

# Start task

# INSTRUCTIONS

generalInstructionsPg1.draw()
win.flip()
event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press or until max time allowed

generalInstructionsPg2.draw()
win.flip()
event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press or until max time allowed

generalInstructionsPg3.draw()
win.flip()
event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press or until max time allowed

blankScreen.draw()
win.flip()
core.wait(1)

## LETTER PRACTICE
# 4 trials, set sizes = 2,2,3,3 (order random across participants)
nTletterPractice = 4
setSizes = [2,2,3,3]
random.shuffle(setSizes)

for s in range(len(setSizes)):
    
    tmp = random.sample(letterList, setSizes[s]) # select letters to show
    
    for t in range(setSizes[s]):
        
        
        # show the letters
        letterDisplay.text = tmp[t]
        letterDisplay.draw()
        win.flip()
        core.wait(1) # 1s letter display
        
        if not t == setSizes[s]-1: # dont show isi after the last letter is shown
            fixationScreen.draw()
            win.flip()
            core.wait(.25) # 250ms isi
        
        # show the recall screen and record responses
     
    blankScreen.draw()
    win.flip()
    core.wait(1) # 1s blank screen before letter grid recall screen
    
    # auto draw is on because we want to draw these on each frame.
    Fbox.autoDraw = True
    Hbox.autoDraw = True
    Jbox.autoDraw = True
    Kbox.autoDraw = True
    Lbox.autoDraw = True
    Nbox.autoDraw = True
    Pbox.autoDraw = True
    Qbox.autoDraw = True
    Rbox.autoDraw = True
    Sbox.autoDraw = True
    Tbox.autoDraw = True
    Ybox.autoDraw = True
    blankButtonBox.autoDraw = True
    clearButtonBox.autoDraw = True
    enterButtonBox.autoDraw=True
    F_r1c1.autoDraw = True
    H_r1c2.autoDraw = True
    J_r1c3.autoDraw = True
    K_r2c1.autoDraw = True
    L_r2c2.autoDraw = True
    N_r2c3.autoDraw = True
    P_r3c1.autoDraw = True
    Q_r3c2.autoDraw = True
    R_r3c3.autoDraw = True
    S_r4c1.autoDraw = True
    T_r4c2.autoDraw = True
    Y_r4c3.autoDraw = True
    blankButton.autoDraw = True
    clearButton.autoDraw = True
    enterButton.autoDraw=True
    letterPracticeRecallText.autoDraw=True

    win.flip()



    # RECORD THE LETTERS AND SHOW THEM BACK TO PARTICIPANTS
    # set up the mouse, it will be called "myMouse"
    myMouse = event.Mouse(visible = True, win = win) 
    myMouse.setPos(newPos =[0,0]); # set mouse to be in the middle of the screen


    # initiate the response variable where we will store the participants' responses
    letterRecall = []; 


    # store the possible shapes that participants can click on during the recall period (this doesn't include the enter box)
    boxes =[Fbox, Hbox, Jbox, Kbox, Lbox, Nbox, Pbox, Qbox, Rbox, Sbox, Tbox, Ybox, blankButtonBox, clearButtonBox]
      
    # Because mouse clicks sometimes happen slower than the speed of frames in psychopy, there may be multiple recorded responses during a single
    # mouse click. for example, if a participant clicks on "F", if the mouse click took place over multiple frames (let's say 4), then "F" will be
    # recorded four times, even though the participant clicked it once. Frames in psychopy are around 16.7 ms, whereas the mouseclick make take
    # a little longer than that. To get around this, we do the following:
    minFramesAfterClick = 10 # to prevent re-entering the if loop too early, other wise multiple letters are recorded during a single mouse click
    timeAfterClick = 0 # initiate time after click ot be 0 (will update in the loop below)

    myMouse.clickReset() # make sure mouseclick is reset to [0,0,0]

    while not myMouse.isPressedIn(enterButtonBox): # to exit this, participants must click on the "enter" button. 
        timeAfterClick += 1

        for box in boxes:
            if myMouse.isPressedIn(box) and timeAfterClick >= minFramesAfterClick: # slows things down so that multiple responses are not recorded for a single click
                letterRecall.append(box.name)
                myMouse.clickReset()
                timeAfterClick=0

                if box == clearButtonBox: # if clear button is pressed, reset everything
                   letterRecall=[]
                   Fbox.color="white"
                   Hbox.color="white" 
                   Jbox.color="white"
                   Kbox.color="white" 
                   Lbox.color="white" 
                   Nbox.color="white" 
                   Pbox.color="white" 
                   Qbox.color="white" 
                   Rbox.color="white" 
                   Sbox.color="white"
                   Tbox.color="white" 
                   Ybox.color="white"


        # change clicked boxes to be green (except theblank button, keep it white)
        for box in boxes:
            if box.name in letterRecall and not box.name == blankButtonBox.name:
                box.color = 'green'
     
        # prep the text that shows participant's responses (letters)
        responseText='' 
        for l in range(len(letterRecall)):
            responseText = "%s %s " % (responseText, letterRecall[l])

        # draw the response text
        showLetterResponse.text = responseText    
        showLetterResponse.autoDraw=True
        win.flip()
            
        #print(letterRecall)
        # reset mouse
        myMouse.clickReset() 
        
    # turn off autodraw
    Fbox.autoDraw = False
    Hbox.autoDraw = False
    Jbox.autoDraw = False
    Kbox.autoDraw = False
    Lbox.autoDraw = False
    Nbox.autoDraw = False
    Pbox.autoDraw = False
    Qbox.autoDraw = False
    Rbox.autoDraw = False
    Sbox.autoDraw = False
    Tbox.autoDraw = False
    Ybox.autoDraw = False
    blankButtonBox.autoDraw = False
    clearButtonBox.autoDraw = False
    enterButtonBox.autoDraw=False
    F_r1c1.autoDraw = False
    H_r1c2.autoDraw = False
    J_r1c3.autoDraw = False
    K_r2c1.autoDraw = False
    L_r2c2.autoDraw = False
    N_r2c3.autoDraw = False
    P_r3c1.autoDraw = False
    Q_r3c2.autoDraw = False
    R_r3c3.autoDraw = False
    S_r4c1.autoDraw = False
    T_r4c2.autoDraw = False
    Y_r4c3.autoDraw = False
    blankButton.autoDraw = False
    clearButton.autoDraw = False
    enterButton.autoDraw=False
    showLetterResponse.autoDraw=False
    letterPracticeRecallText.autoDraw=False

    
    # reset box colors
    Fbox.color="white"
    Hbox.color="white" 
    Jbox.color="white"
    Kbox.color="white" 
    Lbox.color="white" 
    Nbox.color="white" 
    Pbox.color="white" 
    Qbox.color="white" 
    Rbox.color="white" 
    Sbox.color="white"
    Tbox.color="white" 
    Ybox.color="white"
    #print(letterRecall)
    
    #show feedback
    
    correctCount = 0
    for l in range(setSizes[s]):
        if letterRecall[l] == tmp[l]:
            correctCount +=1
    
    
    
    letterFeedbackText.text = text = "You recalled %.0f letters correctly out of %.0f." % (correctCount, setSizes[s])
    letterFeedbackText.draw()
    win.flip()
    core.wait(1.5) # show feedback for 1.5 seconds
    
    blankScreen.draw()
    win.flip()
    core.wait(1) # blank screen for 1s before moving to next trial
    
    
    
    
    
    
    
    
    
    
    
    


# Draw recall screen where letters are shown in a grid along with the enter, blank, and clear buttons
# auto draw is on because we want to draw these on each frame.
# Fbox.autoDraw = True
# Hbox.autoDraw = True
# Jbox.autoDraw = True
# Kbox.autoDraw = True
# Lbox.autoDraw = True
# Nbox.autoDraw = True
# Pbox.autoDraw = True
# Qbox.autoDraw = True
# Rbox.autoDraw = True
# Sbox.autoDraw = True
# Tbox.autoDraw = True
# Ybox.autoDraw = True
# blankButtonBox.autoDraw = True
# clearButtonBox.autoDraw = True
# enterButtonBox.autoDraw=True
# F_r1c1.autoDraw = True
# H_r1c2.autoDraw = True
# J_r1c3.autoDraw = True
# K_r2c1.autoDraw = True
# L_r2c2.autoDraw = True
# N_r2c3.autoDraw = True
# P_r3c1.autoDraw = True
# Q_r3c2.autoDraw = True
# R_r3c3.autoDraw = True
# S_r4c1.autoDraw = True
# T_r4c2.autoDraw = True
# Y_r4c3.autoDraw = True
# blankButton.autoDraw = True
# clearButton.autoDraw = True
# enterButton.autoDraw=True

# win.flip()



# RECORD THE LETTERS AND SHOW THEM BACK TO PARTICIPANTS
# set up the mouse, it will be called "myMouse"
# myMouse = event.Mouse(visible = True, win = win) 
# myMouse.setPos(newPos =[0,0]); # set mouse to be in the middle of the screen


# # initiate the response variable where we will store the participants' responses
# letterRecall = []; 


# # store the possible shapes that participants can click on during the recall period (this doesn't include the enter box)
# boxes =[Fbox, Hbox, Jbox, Kbox, Lbox, Nbox, Pbox, Qbox, Rbox, Sbox, Tbox, Ybox, blankButtonBox, clearButtonBox]
  
# # Because mouse clicks sometimes happen slower than the speed of frames in psychopy, there may be multiple recorded responses during a single
# # mouse click. for example, if a participant clicks on "F", if the mouse click took place over multiple frames (let's say 4), then "F" will be
# # recorded four times, even though the participant clicked it once. Frames in psychopy are around 16.7 ms, whereas the mouseclick make take
# # a little longer than that. To get around this, we do the following:
# minFramesAfterClick = 10 # to prevent re-entering the if loop too early, other wise multiple letters are recorded during a single mouse click
# timeAfterClick = 0 # initiate time after click ot be 0 (will update in the loop below)

# myMouse.clickReset() # make sure mouseclick is reset to [0,0,0]

# while not myMouse.isPressedIn(enterButtonBox): # to exit this, participants must click on the "enter" button. 
#     timeAfterClick += 1

#     for box in boxes:
#         if myMouse.isPressedIn(box) and timeAfterClick >= minFramesAfterClick: # slows things down so that multiple responses are not recorded for a single click
#             letterRecall.append(box.name)
#             myMouse.clickReset()
#             timeAfterClick=0

#             if box == clearButtonBox: # if clear button is pressed, reset everything
#                letterRecall=[]
#                Fbox.color="white"
#                Hbox.color="white" 
#                Jbox.color="white"
#                Kbox.color="white" 
#                Lbox.color="white" 
#                Nbox.color="white" 
#                Pbox.color="white" 
#                Qbox.color="white" 
#                Rbox.color="white" 
#                Sbox.color="white"
#                Tbox.color="white" 
#                Ybox.color="white"


#     # change clicked boxes to be green (except theblank button, keep it white)
#     for box in boxes:
#         if box.name in letterRecall and not box.name == blankButtonBox.name:
#             box.color = 'green'
 
#     # prep the text that shows participant's responses (letters)
#     responseText='' 
#     for l in range(len(letterRecall)):
#         responseText = "%s %s " % (responseText, letterRecall[l])

#     # draw the response text
#     showLetterResponse.text = responseText    
#     showLetterResponse.autoDraw=True
#     win.flip()
        
        
#     # reset mouse
#     myMouse.clickReset() 
        

    
win.close()



## OPERATION STIMULI

