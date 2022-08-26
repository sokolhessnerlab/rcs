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
    
subID = '001'


# Import modules we need
import os, random, time
import pandas as pd
import numpy as np
from psychopy import visual, core, event, monitors
import statistics
#import numpy as np

# change directory
os.chdir('/Users/hayley/Documents/Github/rcs/wmTask') # hb mac

# import files
practiceOperations = pd.read_excel('/Users/hayley/Documents/GitHub/rcs/wmTask/practiceOperations.xlsx')
operationSet1 = pd.read_excel('/Users/hayley/Documents/GitHub/rcs/wmTask/operationSet1.xlsx')
operationSet2 = pd.read_excel('/Users/hayley/Documents/GitHub/rcs/wmTask/operationSet2.xlsx')
#correctMathAns = pd.read_excel('/Users/hayley/Documents/GitHub/rcs/wmTask/correctAnswer.xlsx')

operationSet1.columns = ["weight", "problem", "Sum1", "difficulty"]# fix column names
operationSet1 = operationSet1[operationSet1['weight'] ==1] # removing operations we wont use

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
    text= "In this experiment you will try to memorize letters you see on the screen while you also solve simple math problems. \n\nIn the next few minutes, you will have some practice to get you familiar with how the experiment works. \n\nWe will begin by practicing the letter part of the experiment. \n\n\nPress 'enter' to continue.",
    pos = center,
    color="white",
    height = textHeight, 
    wrapWidth=wrap,
    alignText="left"
)

generalInstructionsPg2 = visual.TextStim(
    win,
    text= "For this practice set, letters will appear on the screen one at a time. \n\nTry to remember each letter in the order presented. \n\nAfter 2-3 letters have been shown, you will see a screen listing 12 possible letters. \n\nYour job is to select each letter in the order presented. \n\nTo do this, use the mouse to select the box for each letter. \n\nThe letters you select will appear at the bottom of the screen. \n\n\nPress 'enter' to continue.",
    pos = center,
    color="white",
    height = textHeight,
    wrapWidth=wrap,
    alignText="left"
)

generalInstructionsPg3 = visual.TextStim(
    win,
    text = "When you have selected all the letters, and they are in the correct order, hit the ENTER box at the bottom right of the screen. \n\nIf you make a mistake, hit the CLEAR box to start over. \n\nIf you forget one of the letters, click the BLANK box to mark the spot for the missing letter. \n\nRemember, it is very important to get the letters in the same order as you see them. \n\nIf you forget one, use the BLANK box to mark the position. \n\nPlease ask the experimenter any questions you may have at this time. \n\n\nWhen you're ready, press 'enter' to start the letter practice.",
    pos = center,
    color="white",
    height = textHeight,
    wrapWidth=wrap,
    alignText="left"
)


mathInstructionsPg1 = visual.TextStim(
    win,
    text= "Now you will practice doing the math part of the experiment.\n\nA math problem will appear on the screen, like this: (2 x 1) + 1 = ? \n\nAs soon as you see the math problem, you should compute the correct answer. \n\nIn the above problem, the answer 3 is correct. \n\nWhen you know the correct answer, you will click the mouse button.\n\nPress 'enter' to continue.",
    pos = center,
    color="white",
    height = textHeight,
    wrapWidth=wrap,
    alignText="left"
)

mathInstructionsPg2 = visual.TextStim(
    win,
    text= "You will see a number displayed on the next screen, along with a box marked TRUE and a box marked FALSE. \n\nIf the number on the screen is the correct answer to the math problem, click on the TRUE box with the mouse. \n\nIf the number is not the correct answer, click on the FALSE box. \n\nFor example, if you see the problem (2 x 2) + 1 = ? and the number on the following screen is 5 click the TRUE box, because the answer is correct. \n\nIf you see the problem (2 x 2) + 1 = ? and the number on the next screen is 6 click the FALSE box, because the correct answer is 5, not 6. \n\nAfter you click on one of the boxes, the computer will tell you if you made the right choice. \n\nPress 'enter' to continue",
    pos = center,
    color="white",
    height = textHeight,
    wrapWidth=wrap,
    alignText="left"
)

mathInstructionsPg3 = visual.TextStim(
    win,
    text= "It is VERY important that you get the math problems correct. \n\nIt is also important that you try and solve the problem as quickly as you can. \n\nPlease ask the experimenter any questions you may have at this time. \n\n\nWhen you're ready, press 'enter' to try some practice problems.",
    pos = center,
    color="white",
    height = textHeight,
    wrapWidth=wrap,
    alignText="left"
)


letterMathPractInstructionsPg1= visual.TextStim(
    win,
    text= "Now you will practice doing both parts of the experiment at the same time. \n\nIn the next practice set, you will be given one of the math problems. \n\nOnce you make your decision about the math problem, a letter will appear on the screen.  \n\nTry and remember the letter.\n\n\nClick 'enter' to continue.",
    pos = center,
    color="white",
    height = textHeight,
    wrapWidth=wrap,
    alignText="left"
)


letterMathPractInstructionsPg2= visual.TextStim(
    win,
    text= "In the previous section where you only solved math problems, the computer computed your average time to solve the problems.\n\nIf you take longer than your average time, the computer will automatically move you onto the letter part, thus skipping the True or False part and will count that problem as a math error. \n\nTherefore it is VERY important to solve the problems as quickly and as accurately as possible. After the letter goes away, another math problem will appear, and then another letter until the trial is complete.\n\nClick 'enter' to continue.",
    pos = center,
    color="white",
    height = textHeight,
    wrapWidth=wrap,
    alignText="left"
)


letterMathPractInstructionsPg3= visual.TextStim(
    win,
    text= "At the end of each set of letters and math problems, a recall screen will appear.\n\nUse the mouse to select the letters you just saw.\n\nTry your best to get the letters in the correct order.\n\nIt is important to work QUICKLY and ACCURATELY on the math.\n\nMake sure you know the answer to the math problem before clicking to the next screen. \n\nYou will not be told if your answer to the math problem is correct. \n\nAfter the recall screen, you will be given feedback about your performance regarding both the number of letters recalled and the percent correct on the math problems. \n\nPlease ask the experimenter any questions you may have at this time.\n\nClick 'enter' to continue.",
    pos = center,
    color="white",
    height = textHeight,
    wrapWidth=wrap,
    alignText="left"
)

letterMathPractInstructionsPg4= visual.TextStim(
    win,
    text= "During the feedback, you will see a number in red in the top right of the screen. \n\nThis indicates your percent correct for the math problems for the entire experiment. \n\nIt is VERY important for you to keep this at least at 85%. \n\nFor our purposes, we can only use data where the participant was at least 85% accurate on the math. \n\nTherefore, in order for you to be asked to come back for future experiments, you must perform at least at 85% on the math problems WHILE doing your best to recall as many letters as possible. \n\nPlease ask the experimenter any questions you may have at this time. \n\nClick 'enter'' to try some practice problems.",
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

## OPERATION STIMULI
mathText = visual.TextStim(
    win, 
    pos = [0,scrnsize[1]*.2],
    color="white",
    height = boxLetterSize,
    wrapWidth = wrap
)

mathPracticeClickEnter = visual.TextStim(
    win, 
    pos = [0,scrnsize[1]*-.4],
    color="white",
    height = textHeight,
    text= "When you have solved the math problem, click the mouse to continue.",
    wrapWidth=wrap
)

mathTrueButton = visual.TextStim(
    win, 
    text='TRUE', 
    pos = [scrnsize[0]*-.3,scrnsize[1]*-.2],
    color="black", 
    height=70
)

mathTrueBox = visual.Rect(
    win, 
    width=boxLetterSize*3, 
    height=boxLetterSize*1.5, 
    units='pix', 
    pos=mathTrueButton.pos, 
    fillColor="white",
    name = "True"
)

mathFalseButton= visual.TextStim(
    win, 
    text='FALSE', 
    pos = [scrnsize[0]*.3,scrnsize[1]*-.2],
    color="black", 
    height=70
)
mathFalseBox = visual.Rect(
    win, 
    width=boxLetterSize*3, 
    height=boxLetterSize*1.5, 
    units='pix', 
    pos=mathFalseButton.pos, 
    fillColor="white",
    name="False"
)

mathPracFeedback = visual.TextStim(
    win,
    pos = [0,scrnsize[1]*-.4],
    color="blue",
    height = textHeight
)

mathSuggestedAns = visual.TextStim(
    win,
    pos = [0,scrnsize[1]*.2],
    color="white",
    height = boxLetterSize
)

mathErrorsAfterRecall = visual.TextStim(
    win, 
    pos = [0,scrnsize[1]*-.2], 
    color="white",
    height = textHeight
)

mathTotalPercentCorrect = visual.TextStim(
    win,
    pos = [scrnsize[0]*.4, scrnsize[1]*.4],
    color="red",
    height = textHeight
)

# # Start letter practice

# # INSTRUCTIONS

# generalInstructionsPg1.draw()
# win.flip()
# event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press or until max time allowed

# generalInstructionsPg2.draw()
# win.flip()
# event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press or until max time allowed

# generalInstructionsPg3.draw()
# win.flip()
# event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press or until max time allowed

# blankScreen.draw()
# win.flip()
# core.wait(1)

# ## LETTER PRACTICE
# # 4 trials, set sizes = 2,2,3,3 (order random across participants)
# nTletterPractice = 4
# setSizes = [2,2,3,3]
# random.shuffle(setSizes)
# #lettersRecall = []
# #lettersShown = []

# letterPracticeData = [] # create data structure with column names
# letterPracticeData.append(
#     [
#         "setSize", 
#         "lettersShown",
#         "response",
#         "responseCorrect",
#         "trial"
#     ]
# )

# for s in range(len(setSizes)):
    
#     tmpLettersShown = random.sample(letterList, setSizes[s]) # select letters to show
    
#     for t in range(setSizes[s]):
        
        
#         # show the letters
#         letterDisplay.text = tmpLettersShown[t]
#         letterDisplay.draw()
#         win.flip()
#         core.wait(1) # 1s letter display
        
#         if not t == setSizes[s]-1: # dont show isi after the last letter is shown
#             fixationScreen.draw()
#             win.flip()
#             core.wait(.25) # 250ms isi
        
#         # show the recall screen and record responses
     
#     blankScreen.draw()
#     win.flip()
#     core.wait(1) # 1s blank screen before letter grid recall screen
    
#     # auto draw is on because we want to draw these on each frame.
#     Fbox.autoDraw = True
#     Hbox.autoDraw = True
#     Jbox.autoDraw = True
#     Kbox.autoDraw = True
#     Lbox.autoDraw = True
#     Nbox.autoDraw = True
#     Pbox.autoDraw = True
#     Qbox.autoDraw = True
#     Rbox.autoDraw = True
#     Sbox.autoDraw = True
#     Tbox.autoDraw = True
#     Ybox.autoDraw = True
#     blankButtonBox.autoDraw = True
#     clearButtonBox.autoDraw = True
#     enterButtonBox.autoDraw=True
#     F_r1c1.autoDraw = True
#     H_r1c2.autoDraw = True
#     J_r1c3.autoDraw = True
#     K_r2c1.autoDraw = True
#     L_r2c2.autoDraw = True
#     N_r2c3.autoDraw = True
#     P_r3c1.autoDraw = True
#     Q_r3c2.autoDraw = True
#     R_r3c3.autoDraw = True
#     S_r4c1.autoDraw = True
#     T_r4c2.autoDraw = True
#     Y_r4c3.autoDraw = True
#     blankButton.autoDraw = True
#     clearButton.autoDraw = True
#     enterButton.autoDraw=True
#     letterPracticeRecallText.autoDraw=True

#     win.flip()



#     # RECORD THE LETTERS AND SHOW THEM BACK TO PARTICIPANTS
#     # set up the mouse, it will be called "myMouse"
#     myMouse = event.Mouse(visible = True, win = win) 
#     myMouse.setPos(newPos =[0,0]); # set mouse to be in the middle of the screen


#     # initiate the response variable where we will store the participants' responses
#     tmpLetterRecall = []; 

#     # store the possible shapes that participants can click on during the recall period (this doesn't include the enter box)
#     boxes =[Fbox, Hbox, Jbox, Kbox, Lbox, Nbox, Pbox, Qbox, Rbox, Sbox, Tbox, Ybox, blankButtonBox, clearButtonBox]
      
#     # Because mouse clicks sometimes happen slower than the speed of frames in psychopy, there may be multiple recorded responses during a single
#     # mouse click. for example, if a participant clicks on "F", if the mouse click took place over multiple frames (let's say 4), then "F" will be
#     # recorded four times, even though the participant clicked it once. Frames in psychopy are around 16.7 ms, whereas the mouseclick make take
#     # a little longer than that. To get around this, we do the following:
#     minFramesAfterClick = 10 # to prevent re-entering the if loop too early, other wise multiple letters are recorded during a single mouse click
#     timeAfterClick = 0 # initiate time after click ot be 0 (will update in the loop below)

#     myMouse.clickReset() # make sure mouseclick is reset to [0,0,0]

#     while not myMouse.isPressedIn(enterButtonBox): # to exit this, participants must click on the "enter" button. 
#         timeAfterClick += 1

#         for box in boxes:
#             if myMouse.isPressedIn(box) and timeAfterClick >= minFramesAfterClick: # slows things down so that multiple responses are not recorded for a single click
#                 tmpLetterRecall.append(box.name)
#                 myMouse.clickReset()
#                 timeAfterClick=0

#                 if box == clearButtonBox: # if clear button is pressed, reset everything
#                    tmpLetterRecall=[]
#                    Fbox.color="white"
#                    Hbox.color="white" 
#                    Jbox.color="white"
#                    Kbox.color="white" 
#                    Lbox.color="white" 
#                    Nbox.color="white" 
#                    Pbox.color="white" 
#                    Qbox.color="white" 
#                    Rbox.color="white" 
#                    Sbox.color="white"
#                    Tbox.color="white" 
#                    Ybox.color="white"


#         # change clicked boxes to be green (except theblank button, keep it white)
#         for box in boxes:
#             if box.name in tmpLetterRecall and not box.name == blankButtonBox.name:
#                 box.color = 'green'
     
#         # prep the text that shows participant's responses (letters)
#         responseText='' 
#         for l in range(len(tmpLetterRecall)):
#             responseText = "%s %s " % (responseText, tmpLetterRecall[l])

#         # draw the response text
#         showLetterResponse.text = responseText    
#         showLetterResponse.autoDraw=True
#         win.flip()
            

#         # reset mouse
#         myMouse.clickReset() 
        
#     # turn off autodraw
#     Fbox.autoDraw = False
#     Hbox.autoDraw = False
#     Jbox.autoDraw = False
#     Kbox.autoDraw = False
#     Lbox.autoDraw = False
#     Nbox.autoDraw = False
#     Pbox.autoDraw = False
#     Qbox.autoDraw = False
#     Rbox.autoDraw = False
#     Sbox.autoDraw = False
#     Tbox.autoDraw = False
#     Ybox.autoDraw = False
#     blankButtonBox.autoDraw = False
#     clearButtonBox.autoDraw = False
#     enterButtonBox.autoDraw=False
#     F_r1c1.autoDraw = False
#     H_r1c2.autoDraw = False
#     J_r1c3.autoDraw = False
#     K_r2c1.autoDraw = False
#     L_r2c2.autoDraw = False
#     N_r2c3.autoDraw = False
#     P_r3c1.autoDraw = False
#     Q_r3c2.autoDraw = False
#     R_r3c3.autoDraw = False
#     S_r4c1.autoDraw = False
#     T_r4c2.autoDraw = False
#     Y_r4c3.autoDraw = False
#     blankButton.autoDraw = False
#     clearButton.autoDraw = False
#     enterButton.autoDraw=False
#     showLetterResponse.autoDraw=False
#     letterPracticeRecallText.autoDraw=False

    
#     # reset box colors
#     Fbox.color="white"
#     Hbox.color="white" 
#     Jbox.color="white"
#     Kbox.color="white" 
#     Lbox.color="white" 
#     Nbox.color="white" 
#     Pbox.color="white" 
#     Qbox.color="white" 
#     Rbox.color="white" 
#     Sbox.color="white"
#     Tbox.color="white" 
#     Ybox.color="white"

    
#     #show feedback    
#     correctCount = 0
#     if len(tmpLetterRecall) == len(tmpLettersShown): # if participant recalls correct number of letters
#         for l in range(setSizes[s]):
#             if tmpLetterRecall[l] == tmpLettersShown[l]:
#                 correctCount +=1
#         letterFeedbackText.text = text = "You recalled %.0f letters correctly out of %.0f." % (correctCount, setSizes[s])
#     elif len(tmpLetterRecall) > len(tmpLettersShown): # if sub recalls more letters than set size
#         for l in range(setSizes[s]):
#             if tmpLetterRecall[l] == tmpLettersShown[l]:
#                 correctCount +=1
#         letterFeedbackText.text = text = "You recalled %.0f letters correctly out of %.0f but recalled too many letters." % (correctCount, setSizes[s])
#     elif len(tmpLetterRecall)==0: # if participant does not recall any letters
#         letterFeedbackText.text = text = "You did not recall any letters."
#     elif (len(tmpLetterRecall)<len(tmpLettersShown)) and not (len(tmpLetterRecall) ==0):
#         for l in range(setSizes[s]):
#             if tmpLetterRecall[l] == tmpLettersShown[l]:
#                 correctCount +=1
#         letterFeedbackText.text = text = "You recalled %.0f letters correctly out of %.0f but did not recall enough letters." % (correctCount, setSizes[s])


#     letterFeedbackText.text = text = "You recalled %.0f letters correctly out of %.0f." % (correctCount, setSizes[s])
#     letterFeedbackText.draw()
#     win.flip()
#     core.wait(1.5) # show feedback for 1.5 seconds
    
#     blankScreen.draw()
#     win.flip()
#     core.wait(1) # blank screen for 1s before moving to next trial
    
#     # after each trial, add data for:
#     #lettersRecall.append(tmpLetterRecall) # recalled letters
#     #lettersShown.append(tmpLettersShown) # letters displayed 
   
#     letterPracticeData.append(
#         [
#             setSizes[s], 
#             tmpLettersShown,
#             tmpLetterRecall,
#             correctCount,
#             s
#         ]
#     )
    
# # change practice file into pandas dataframe
# letterPracticeData = pd.DataFrame(letterPracticeData) #convert data into pandas dataframe
# letterPracticeData.columns=["setSize","lettersShown","lettersRecall","correctCount","trial"] # add column names
# letterPracticeData = letterPracticeData.iloc[1: , :] # drop the first row which are the variable names



# # OPERATION PRACTICE
# # Instructions:
# mathInstructionsPg1.draw()
# win.flip()
# event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press or until max time allowed

# mathInstructionsPg2.draw()
# win.flip()
# event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press or until max time allowed

# mathInstructionsPg3.draw()
# win.flip()
# event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press or until max time allowed

# blankScreen.draw()
# win.flip()
# core.wait(1)


# # start math practice (15 trials, math operations only)
# nTrials = 15
 
# # set up mouse for true/false responses
# myMouse = event.Mouse(visible = True, win = win) 
# minFramesAfterClick = 10 # to prevent re-entering the if loop too early, other wise multiple letters are recorded during a single mouse click
# timeAfterClick = 0
# mathboxes = [mathTrueBox, mathFalseBox]


# mathPracticeData = [] # create data structure with column names
# mathPracticeData.append(
#     [
#         "operation", 
#         "response",
#         "responseCorrect",
#         "solveMathRT",
#         "suggestedAnswer",
#         "suggestAnswerCorrect",
#         "trueFalseRT",
#         "trial"
#     ]
# )


# for m in range(nTrials):

#     # set the text for the problem and suggested answer on this trial
#     selectedMathProblem = practiceOperations.problemPractice[m]
#     mathSuggestedAns.text = str(practiceOperations.suggestAnsPractice[m])

#     blankScreen.draw()
#     win.flip()
#     core.wait(.5) # blank screen for 500ms prior to each math operation
    

#     # Show the math problem
#     #selectedMathProblem = text = "%s %s %s = ?" % (selectedOps1.problem[m], selectedOps2.Sign[m], selectedOps2.Op2[m])
    
#     mathText.text = selectedMathProblem
#     mathText.draw()
#     mathPracticeClickEnter.draw()
#     buttons = [0]*len(event.mouseButtons) #initializes it to a list of 0s with the length equal to the number of active buttons.
#     myMouse.setPos(newPos =[0,mathFalseBox.pos[1]]); # set mouse to be in the middle of the true/false buttons

    
#     win.flip() # show suggested answer
#     myMouse.clickReset() # make sure mouseclick is reset to [0,0,0], restarts the clock
    
#     while not any(buttons):
#         (buttons,rtTimes) = myMouse.getPressed(getTime=True)
   
#     #tmpMathRT.append(rtTimes[0])
#     tmpMathRT = rtTimes[0]
    
#     #Draw the isi
#     fixationScreen.draw() 
#     win.flip()
#     core.wait(.2) # 200ms isi
    

#     # Show the suggested answer on screen along with "true" and "false" buttons
#     mathSuggestedAns.draw()
#     mathTrueBox.draw()
#     mathTrueButton.draw()
#     mathFalseBox.draw()
#     mathFalseButton.draw() 
    
#     myMouse.setPos(newPos =[0,mathFalseBox.pos[1]]); # set mouse to be in the middle of the true/false buttons
#     win.flip()

#     # collect response, record RT and check whether participant was correct.
#     myMouse.clickReset() # make sure mouseclick is reset to [0,0,0]

#     mouseResponse = 0;
    
#     while mouseResponse == 0:        
#         timeAfterClick += 1

#         for box in mathboxes:
#             if myMouse.isPressedIn(box) and timeAfterClick >= minFramesAfterClick: # slows things down so that multiple responses are not recorded for a single click
#                 buttons, times = myMouse.getPressed(getTime=True)
#                 tmpMathResp = box.name
#                 tmpMathRTtrueFalse = times[0]
#                 #tmpMathResp.append(box.name) # was true or false clicked
#                 #tmpMathRTtrueFalse.append(times[0]) # store RT
                
#                 # once pressed, change box color to grey, redraw everything
#                 box.color = "grey"
#                 mathSuggestedAns.draw()
#                 mathTrueBox.draw()
#                 mathTrueButton.draw()
#                 mathFalseBox.draw()
#                 mathFalseButton.draw() 
                
                
#                 # Show “correct” or “incorrect” on the true/false screen for 500ms
#                 if tmpMathResp == str(practiceOperations.correctRespPractice[m]):
#                     respCorrect = 1
#                     mathPracFeedback.text = "Correct"
#                 else:
#                     respCorrect = 0
#                     mathPracFeedback.text = "Incorrect"
                
#                 mathPracFeedback.draw()
#                 win.flip()
#                 core.wait(.5)
                
#                 box.color = "white" # reset box color to white
#                 myMouse.clickReset()
#                 timeAfterClick=0
#                 mouseResponse =1 # change to 1 to end while loop

#     mathPracticeData.append(
#         [
#             selectedMathProblem, 
#             tmpMathResp,
#             respCorrect,
#             tmpMathRT,
#             practiceOperations.suggestAnsPractice[m],
#             practiceOperations.correctRespPractice[m],
#             tmpMathRTtrueFalse,
#             m
#         ]
#     )
    
    
# # Reformat data to pandas dataframe
# mathPracticeData = pd.DataFrame(mathPracticeData)
# mathPracticeData.columns = ["operation","response","responseCorrect", "solveMathRT","suggestedAnswer", "suggestAnswerCorrect","trueFalseRT","trial"]
# mathPracticeData = mathPracticeData.iloc[1: , :] # drop the first row which are the variable names

# # calculate the cut off time for following sections of the task: average RT + 2.5* standard deviation RT
# correctMathDF = mathPracticeData.loc[mathPracticeData["responseCorrect"]==1]
# avgRT = statistics.mean(correctMathDF["solveMathRT"])
# stdRT = statistics.stdev(correctMathDF["solveMathRT"])

# maxMathDisplay = avgRT + (2.5*stdRT) # calculate the max display for the math problems in the future sets
# mathPracticeData["maxMathDisp"] = maxMathDisplay # save to the dataframe



# # Start letter + math practice

# # INSTRUCTIONS

# letterMathPractInstructionsPg1.draw()
# win.flip()
# event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press or until max time allowed

# letterMathPractInstructionsPg2.draw()
# win.flip()
# event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press or until max time allowed

# letterMathPractInstructionsPg3.draw()
# win.flip()
# event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press or until max time allowed

# letterMathPractInstructionsPg4.draw()
# win.flip()
# event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press or until max time allowed

# blankScreen.draw()
# win.flip()
# core.wait(1)



#Start Letter + Math practice

maxMathDisplay = 4# for testing

#MATH SET UP
nTbothPractice = 3 # three trials for the letter-math practice
setSize = 2 # all trials are 2 letter-math pairs

# Select math problems
selectedOps1 = operationSet1.sample(n=nTbothPractice*setSize,axis = "rows")
selectedOps2 = operationSet2.sample(n=nTbothPractice*setSize, axis="rows", replace="True")
selectedOps1.index=range(nTbothPractice*setSize)
selectedOps2.index=range(nTbothPractice*setSize)
operationsLettersDF = pd.concat([selectedOps1, selectedOps2], axis=1) # combine dataframes into one
correctAnswerMath =[]
suggestedAnswerMath=[]
totalSumTmp = []

# Make sure that the sum of operation 1 (e.g. (2/2)) and operation 2 (e.g. -5) are greater than zero, if not
# add three to the second operation until the sum is greater than 0
for o in range(nTbothPractice*setSize):
    totalSum = operationsLettersDF["Sum1"][o] + operationsLettersDF["Sum2"][o]
    
    while totalSum <=0:
        operationsLettersDF["Sum2"][o] = operationsLettersDF["Sum2"][o] + 3
        totalSum = operationsLettersDF["Sum1"][o] + operationsLettersDF["Sum2"][o]
    
    operationsLettersDF["Op2"][o] = abs(operationsLettersDF["Sum2"][o]) # update the operation 2 if sum2 changed
    
    # if making the sum of the two operations changes the second operation +, then we need to change the sign for that operation
    if operationsLettersDF["Sum2"][o] > 0:
        operationsLettersDF["Sign"][o] = "+"
        
    # determine whether suggested answer is correct (0=incorrect, 1=correct)
    correctAnswerMath.append(random.randint(0,1)) 
    
    # determine the suggested answer that will be shown
    if correctAnswerMath[o]==1:
        suggestedAnswerMath.append(totalSum)
    elif correctAnswerMath[o] ==0:
        randNum = random.randint(-25,25) # pick a random number
        while totalSum + randNum <0 or totalSum + randNum == totalSum:
            randNum = randNum + 2
            #print(randNum)
        
        suggestedAnswerMath.append(totalSum + randNum)
    totalSumTmp.append(totalSum)

operationsLettersDF["totalSum"] = totalSumTmp # save the true sum to the big df
operationsLettersDF["showCorrectAns"]= correctAnswerMath # save correctAnswerMath variable to selectedOps2
operationsLettersDF["suggestedAnswerMath"]= suggestedAnswerMath # save suggestedAnswerMath variable to selectedOps2
operationsLettersDF["setSize"] = setSize # set sizes are the same for practice, all =2
operationsLettersDF["trialPerSet"] = [0,1]*nTbothPractice # operation number in each set
operationsLettersDF["setNumber"] = [0,0,1,1,2,2]


# LETTER SET UP
bothPracticeLetters = []
lettersShownShortFormat = [] # each row has all letters shown
# select the letters we will show on each trial
for t in range(nTbothPractice):
    tmpLetters = random.sample(letterList, k = setSize)# randomly select two letters, using sample instead of choices does without replacement
    # we don't want to have repeat letters in a single trial^
    lettersShownShortFormat.append(tmpLetters) # save them in short format
    for s in range(len(tmpLetters)):
        bothPracticeLetters.append(tmpLetters[s]) # also save letters in long format

operationsLettersDF["lettersShown"] = bothPracticeLetters # add letters that are shown following each math operation



# Set up mouse
myMouse = event.Mouse(visible = True, win = win) 
minFramesAfterClick = 10 # to prevent re-entering the if loop too early, other wise multiple letters are recorded during a single mouse click
timeAfterClick = 0
mathboxes = [mathTrueBox, mathFalseBox]


bothPracticeData = [] # create data structure with column names
bothPracticeData.append(
    [
        "operation1", 
        "sum1",
        "operation2",
        "sign",
        "sum2",
        "totalSum",
        "showCorrectAns",
        "suggestedAnswer",
        "mathResponse",
        "mathResponseCorrect",
        "solveMathRT",
        "trueFalseRT",
        "setSize",
        "setNumber",
        "trialPerSet",
        "lettersShown",
        "lettersRecall",
        "correctCount"
        
    ]
)




for t in range(nTbothPractice): # for each trial
    for s in range(setSize): # and set size within each trial
        
        #pull out row we need for each trial/set
        tmpRow = operationsLettersDF.loc[(operationsLettersDF.setNumber ==t) & (operationsLettersDF.trialPerSet==s)]

    # set the text for the problem and suggested answer on this trial
        selectedMathProblem = "%s %s %s = ?" % (tmpRow.problem.iat[0], tmpRow.Sign.iat[0], tmpRow.Op2.iat[0])
        mathSuggestedAns.text = str(tmpRow.suggestedAnswerMath.iat[0])
    
        blankScreen.draw()
        win.flip()
        core.wait(.5) # blank screen for 500ms prior to each math operation
        
    #draw the math problem
        mathText.text = selectedMathProblem
        mathText.draw()
        mathPracticeClickEnter.draw()
        buttons = [0]*len(event.mouseButtons) #initializes it to a list of 0s with the length equal to the number of active buttons.
        myMouse.setPos(newPos =[0,mathFalseBox.pos[1]]); # set mouse to be in the middle of the true/false buttons
    
        
        win.flip() # show the math problem
        myMouse.clickReset() # make sure mouseclick is reset to [0,0,0], restarts the clock
        mathMaxClock = core.Clock() # start the clock
    
    # wait for math response to move onto math T/F
        while not any(buttons) and mathMaxClock.getTime() <= maxMathDisplay:
            (buttons,rtTimes) = myMouse.getPressed(getTime=True)
       
       #if participant does not respond in time on math, move to letter part
        if not any(buttons): 
            tmpMathRT = float("nan") # record RT as nan
            tmpMathResp = float("nan")
            respCorrect = 0
            tmpMathRTtrueFalse = float("nan")
            
            # record data
            bothPracticeData.append(
                [
                    tmpRow.problem.iat[0], 
                    tmpRow.Sum1.iat[0],
                    tmpRow.Op2.iat[0],
                    tmpRow.Sign.iat[0],
                    tmpRow.Sum2.iat[0],
                    tmpRow.totalSum.iat[0],
                    tmpRow.showCorrectAns.iat[0],
                    tmpRow.suggestedAnswerMath.iat[0],
                    tmpMathResp,
                    respCorrect,
                    tmpMathRT,
                    tmpMathRTtrueFalse,
                    tmpRow.setSize.iat[0],
                    tmpRow.trialPerSet.iat[0],
                    tmpRow.lettersShown.iat[0],
                    'l', # tmp place holder for letters recalled
                    0 # tmp place holder for correct count
                    
                ]
            )
            
        else: # if participant does respond in time, move onto True/False
        
        
            tmpMathRT = rtTimes[0]
        
            #Draw the isi
            fixationScreen.draw() 
            win.flip()
            core.wait(.2) # 200ms isi
        
    
            # Show the suggested answer on screen along with "true" and "false" buttons
            mathSuggestedAns.draw()
            mathTrueBox.draw()
            mathTrueButton.draw()
            mathFalseBox.draw()
            mathFalseButton.draw() 
        
            myMouse.setPos(newPos =[0,mathFalseBox.pos[1]]); # set mouse to be in the middle of the true/false buttons
            win.flip()
    
            # collect response, record RT and check whether participant was correct.
            myMouse.clickReset() # make sure mouseclick is reset to [0,0,0]
    
            mouseResponse = 0;
        
            while mouseResponse == 0:        
                timeAfterClick += 1
        
                for box in mathboxes:
                    if myMouse.isPressedIn(box) and timeAfterClick >= minFramesAfterClick: # slows things down so that multiple responses are not recorded for a single click
                        buttons, times = myMouse.getPressed(getTime=True)
                        tmpMathResp = box.name
                        tmpMathRTtrueFalse = times[0]
    
                        
                        # once pressed, change box color to grey, redraw everything
                        box.color = "grey"
                        mathSuggestedAns.draw()
                        mathTrueBox.draw()
                        mathTrueButton.draw()
                        mathFalseBox.draw()
                        mathFalseButton.draw() 
                        
                        
                        # Is response correct or incorrect?
                        if (tmpRow.showCorrectAns.iat[0] ==1) and (tmpMathResp == 'True'):
                            respCorrect = 1
                        elif (tmpRow.showCorrectAns.iat[0] ==0) and (tmpMathResp == 'True'):
                           respCorrect = 0
                        elif (tmpRow.showCorrectAns.iat[0] ==1) and (tmpMathResp == 'False'):
                            respCorrect = 0
                        elif (tmpRow.showCorrectAns.iat[0] ==0) and (tmpMathResp == 'False'):
                            respCorrect = 1
                                            
                        
                        box.color = "white" # reset box color to white
                        myMouse.clickReset() # reset mouse
                        timeAfterClick=0 # reset timeAfterClick
                        mouseResponse =1 # change to 1 to end while loop
        
                        bothPracticeData.append(
                            [
                                tmpRow.problem.iat[0], 
                                tmpRow.Sum1.iat[0],
                                tmpRow.Op2.iat[0],
                                tmpRow.Sign.iat[0],
                                tmpRow.Sum2.iat[0],
                                tmpRow.totalSum.iat[0],
                                tmpRow.showCorrectAns.iat[0],
                                tmpRow.suggestedAnswerMath.iat[0],
                                tmpMathResp,
                                respCorrect,
                                tmpMathRT,
                                tmpMathRTtrueFalse,
                                tmpRow.setSize.iat[0],
                                t,
                                tmpRow.trialPerSet.iat[0],
                                tmpRow.lettersShown.iat[0],
                                'l', # tmp place holder for letters recalled
                                0 # tmp place holder for correct count
                                
                            ]
                        )
                        
        
            
    #LEFT OFF HERE - NEED TO CLEAR SCREEN AND THEN SHOW FEEDBACK - RN FEEDBACK IS SHOWING ON TOP OF T/F SCREEN
    #FEEDBACK AT THE END OF EACH SET (SO AFTER THE LETTER RECAL)
    # feedback here shows both the letter recall, math correct, and overall percent correct in math across sets
    
    # calculate how well participant is doing with math (this is the number that gets displayed at the end)
    tmpDF = pd.DataFrame(bothPracticeData) # temporarily make practice data a dataframe for easier handling (this gets overwritten after each set)
    tmpDF.columns = tmpDF.iloc[0]
    tmpDF = tmpDF.iloc[1: , :]
    
    mathPercentCorrect = round(tmpDF.mathResponseCorrect.mean()*100) # number to show in red on feedback screen after letter recall
    mathErrorsDuringSet = sum(tmpDF.mathResponseCorrect==0) # number of errors made during the set




    mathErrorsAfterRecall.text = text = "You made %.0f math error(s) for this set of trials." %(mathErrorsDuringSet)
    mathTotalPercentCorrect.text = text = "%.0f%%" %(mathPercentCorrect)
    
    mathErrorsAfterRecall.draw()
    mathTotalPercentCorrect.draw()
    
    win.flip()
    core.wait(2)
        
# select letters:

# Math part
# 1) select math problem and adjust if sum is negative(DONE)
# 2) show math problem, with the maxMathDisplay as the limit (DONE) 
# 3) record RT  (DONE)
# 4) show suggested answer with t/f screen (no feedback given) (DONE)
# 5) record RT and response, save whether it is correct (DONE))
# 6) Keep count of correct math response to show in red on screen (how well sub is doing over a block, not just a set) (DONE)
# 7) be checking if participant is doing well enough continue? is this a thing? warning sub if errors are more than 3 - math or letters or both?
# 8) check whether we add 1000ms to the math display at any point?
# 9) check that max math display is calculated correctly (need a lower limit?)

# Letters part:
# 1) mostly same as letters practice in terms of showing and selecting stimuli
# 2) show feedback for both letters and math at the end of each recall with percent math correct in red in corner of the screen
# 3) warn participant is errors are greater than 3 (math errors? letter errors?)
# 4) right now, participants only get credit if they enter the correct number of letters


win.close()





#---- AT THE END OR IF THINGS BREAK - SAVE THE DATA WE HAVE ----#
# 'finally' this will be outside the 'try' command

# # Reformat data to pandas dataframe if it wasn't above - if it breaks before mathPracticeData was changed to PD, it means the practice trials were not complete and the max math display was not calculated
# if not isinstance(mathPracticeData, pd.DataFrame):
#     mathPracticeData = pd.DataFrame(mathPracticeData)
#     mathPracticeData.columns = ["operation","response","responseCorrect", "solveMathRT","suggestedAnswer", "suggestAnswerCorrect","trueFalseRT","trial"]
#     mathPracticeData = mathPracticeData.iloc[1: , :] # drop the first row which are the variable names

# if not isinstance(letterPracticeData, pd.DataFrame):
#     letterPracticeData = pd.DataFrame(letterPracticeData) #convert data into pandas dataframe
#     letterPracticeData.columns=["setSize","lettersShown","lettersRecall","correctCount","trial"] # add column names
#     letterPracticeData = letterPracticeData.iloc[1: , :] # drop the first row which are the variable namesPracticeData.iloc[1: , :] # drop the first row which are the variable names


# # SAVE THE DATA
# datetime = time.strftime("%Y%m%d-%H%M%S"); # save date and time
# filenameLetterPrac = "rcsOSPANletterPractice_" + "sub" + subID + "_" + datetime + ".csv"; # make filename
# letterPracticeData.to_csv(filenameLetterPrac)

# filenameMathPrac = "rcsOSPANmathPractice_" + "sub" + subID + "_" + datetime + ".csv"; # make filename
# mathPracticeData.to_csv(filenameMathPrac)

#filenameBothPrac ="rcsOSPANbothPractice_" + "sub" + subID + "_" + datetime + ".csv"; # make filename
#bothPracticeData.to_csv(filenameMathPrac)

