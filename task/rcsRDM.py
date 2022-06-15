#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 14:26:15 2022

@author: hayley
"""


"""
Risky decision-making for HRB dissertation project: Risk, context and strategy. 
"""


# notes: the screen dimensions are going to shift when we put on lab computer, so will the stimuli

#def rcsRDM(subID, cond1, cond2, cond1color, cond2color):
subID='001'
cond1 = 1
cond2 = 1
cond1color = 0
cond2color = 1
    

# Import modules we need
import random, time, os
import pandas as pd
from psychopy import visual, core, event, monitors
import numpy as np

# change directory
os.chdir('/Users/hayley/Documents/Github/rcs/task') # hb mac
#os.chdir('/Users/shlab/Documents/Github/rcs/task') # mahimahi
#os.chdir('/Users/Display/Desktop/Github/rcs/task') # tofu
# Import the choice set function
from rcsRDMChoiceSet import *


# Define rounds of risky decision-making task
RDMrounds=2; 

# Store conditions in one structure (0= control, 1 = strategy)
cond = [cond1, cond2]
colorOrder = [cond1color, cond2color]
  

# Set up experimental parameters that are consistent across task rounds:

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
textHeight = radius/2.1
nT = 3 #for testing purposes
#nT = len(safe) # for real


#Locations for drawing line and dollar amounts:

lnGamL =[centerL[0]-radius-2, centerL[0]+radius+2] #x start and end points for line when gamble is on the left
lnGamR = [centerR[0]-radius-2, centerR[0]+radius+2] # x start and end points for line when gamble is on the right

gainGamL = [centerL[0], centerL[1]+(radius*.45)] #position of gain amount when gamble on the left
gainGamR = [centerR[0], centerR[1]+(radius*.45)] #position of gain amount when gamble on the right

lossGamL= [centerL[0], centerL[1]-(radius*.45)] #position of loss amount when gamble on the left
lossGamR= [centerR[0], centerR[1]-(radius*.45)] #position of loss amount when gamble on the right

altGamL = [centerR[0], 100] #position of safe amount when gamble on the left
altGamR = [centerL[0], 100] #position of safe amount when gamble on the right

# Timing stuff
stimTime = 2;
choiceTime = 2;
outcomeTime = 1;
isi = .5;


# set up monitor in lab on mahimahi
# mon = monitors.Monitor("DELL 1908FP")
# mon.setSizePix([1280,1024])
# mon.save()


# Set up the window
win = visual.Window(
    size=scrnsize,
    units="pix",
    fullscr=False,
    color=[-1, -1, -1], #black screen
    screen=1 # on second screen
)

# # Set up the window
# win = visual.Window(
#     size=scrnsize,
#     units="pix",
#     fullscr=False,
#     color=[-1, -1, -1] #black screen
# )


blackBox = visual.Rect(win, width=scrnsize[0]*.95, height=scrnsize[1]*.95, units='pix', pos=[0,0], fillColor='black')
greenBox = visual.Rect(win, width=scrnsize[0], height=scrnsize[1], units='pix', pos=[0,0], fillColor=[0,.6,0])
purpleBox = visual.Rect(win, width=scrnsize[0], height=scrnsize[1], units='pix', pos=[0,0], fillColor=[.5,0,.5])




# Prepare instructions and other task stimuli

mes1 = visual.TextStim(win, text='Setting up...', pos = (0,0),color=[1,1,1], height=40)
mes2 = visual.TextStim(win, text='Waiting for experimenter', pos = (0,0),color=[1,1,1], height =40)
inst1 = visual.TextStim(
    win, 
    text='As discussed, in this task you will choose between a gamble and a guaranteed alternative. \n\nPress "V" to choose the left option and "N" to choose the right option.', 
    pos = (0,0),
    color=[1,1,1],
    height = 40,
    wrapWidth = scrnsize[0]*.75
    )

inst2 = visual.TextStim(
    win, 
    text='Next up are 5 practice trials. \n\nAny questions? \n\nIf so, please ask the experimenter now.', 
    pos = (0,0),
    color=[1,1,1],
    height = 40,
    wrapWidth = scrnsize[0]*.75
    )

inst3 = visual.TextStim(
    win, 
    text='Press "V" or "N" when you are ready to begin the practice.', 
    pos = (0,0),
    color=[1,1,1],
    height = 40,
    wrapWidth = scrnsize[0]*.75
    )

postPrac = visual.TextStim(
    win, 
    text='Practice complete! \n\nAny questions? \n\nIf so, please ask the experimenter now.', 
    pos = (0,0),
    color=[1,1,1],
    height = 40,
    wrapWidth = scrnsize[0]*.75
    )



#   PREPARING FOR THE FIRST ROUND INSTRUCTIONS
prepForConditionRound1 = visual.TextStim(
    win,
    text='Before we begin ROUND 1 of the gambling task, you will be asked to read some additional task instructions. Please let the experimenter know when you are done. \n\n When you are done, you will be asked to verbally share a short summary about the instructions to the experimenter.\n\n\n Press ‘enter’ to continue.',
    pos = (0,0),
    color=[1,1,1],
    height=40,
    wrapWidth=scrnsize[0]*.75
    )


# PREPARING FOR THE SECOND ROUND OF INSTRUCTIONS
# if participant is switching conditions from round 1:
prepForConditionRound2_pg1Switching = visual.TextStim(
    win,
    text='Before we begin ROUND 2 of the gambling task, you will be asked to read additional task instructions that are different from round 1. \n\nThe mechanics of the task will be the exact same but the instructions will ask you to think differently than you did in round 1. \n\n Try your best to forget the instructions from round 1 and follow these new instructions. \n\n\n Press ‘enter’ to continue.',
    pos = (0,0),
    color=[1,1,1],
    height=40,
    wrapWidth=scrnsize[0]*.75
    )

prepForConditionRound2_pg1Repeating= visual.TextStim(
    win,
    text='Before we begin ROUND 2 of the gambling task, you will be asked to read a brief reminder of the instructions that were given in round 1.\n\n\n Press ‘enter’ to continue.',
    pos = (0,0),
    color=[1,1,1],
    height=40,
    wrapWidth=scrnsize[0]*.75
    )

prepForConditionRound2_pg2forAllSubs = visual.TextStim(
    win,
    text='Please let the experimenter know when you are done reading the instructions. \n\nWhen you are done, you will be asked to verbally share a short summary about the instructions to the experimenter.\n\n\nPress ‘enter’ to continue.',
    pos = (0,0),
    color=[1,1,1],
    height=40,
    wrapWidth=scrnsize[0]*.75
    )


# CONTROL INSTRUCTIONS (FIRST TIME AROUND)
controlInst1 = visual.TextStim(
    win,
    text='In this round of the task, please make your choices however you normally would, considering all factors that you naturally would notice or think about. \n\n Previous research has found that people use all kinds of information to make choices in risky contexts. \n\n\nPress ‘enter’ to continue.',
    pos = (0,0),
    color=[1,1,1],
    height=40,
    wrapWidth=scrnsize[0]*.75
    )

controlInst2 = visual.TextStim(
    win,
    text='Knowing how the task works, don’t try to control your thoughts any more than you would normally, and take as much of a natural approach to your decisions as you can, whatever that might mean for you. \n\nMake your choices in a way that makes sense to you, given any goals, rules of thumb, or factors you think or feel are important. \n\n\nPress ‘enter’ to continue.',
    pos = (0,0),
    color=[1,1,1],
    height=40,
    wrapWidth=scrnsize[0]*.75
    )

controlInst3 = visual.TextStim(
    win,
    text='For this round, focus on the task itself, and the events, options, and actions that you would naturally consider, and how you feel about them. \n\nIf you select the gamble, you have an equal chance of receiving either amount and if you select the safe option, that will be the outcome for that trial.\n\nYou will complete many trials in this round.\n\n\nPress ‘enter’ to continue.',
    pos = (0,0),
    color=[1,1,1],
    height=40,
    wrapWidth=scrnsize[0]*.75
    )

controlInst4 = visual.TextStim(
    win,
    text='On each trial, let your thoughts, feelings, impulses, and goals guide your decision-making as naturally as possible, without trying to change, eliminate, or emphasize them beyond how you might otherwise naturally. \n\nRemember that you will be paid the outcome of one randomly selected trial, and simply try to make the best choices you can. \n\nFor this round, approach the task and evaluate your choice options as you would naturally, without trying to control or change your approach. \n\n\nPress ‘enter’ to continue.',
    pos = (0,0),
    color=[1,1,1],
    height=40,
    wrapWidth=scrnsize[0]*.75
    )


controlReminder1  = visual.TextStim(
    win,
    text='As a reminder, in this round of the task, please make your choices however you normally would.\n\n On each trial, let your thoughts, feelings, impulses, and goals guide your decision-making as naturally as possible, without trying to change, eliminate, or emphasize them beyond how you might otherwise naturally. \n\n\nPress ‘enter’ to continue.',
    pos = (0,0),
    color=[1,1,1],
    height=40,
    wrapWidth=scrnsize[0]*.75
    )

controlReminder2 = visual.TextStim(
    win,
    text='Simply try to make the best choices you can.\n\n For this round, approach the task and evaluate your choice options as you would naturally, without trying to control or change your approach.\n\n\nPress ‘enter’ to continue.',
    pos = (0,0),
    color=[1,1,1],
    height=40,
    wrapWidth=scrnsize[0]*.75
    )


# STRATEGY INSTRUCTIONS (FIRST TIME AROUND)

stratInst1 = visual.TextStim(
    win,
    text='In this round of the task, please make your choices in isolation from any context, considering each choice solely on its own merits. \n\nIn our previous studies involving this gambling task, we have found that participants’ choices to accept the gamble were influenced not only by the options on the current trial but also depended on what happened earlier in the task.\n\n\nPress ‘enter’ to continue.',
    pos = (0,0),
    color=[1,1,1],
    height=40,
    wrapWidth=scrnsize[0]*.75
    )

stratInst2 = visual.TextStim(
    win,
    text='Each trial in this task is unrelated to previous trials. \n\nThe values and outcomes of previous trials do not influence the outcome of the current trial. \n\nAllowing previous values and outcomes to influence your current choice may lead to a lower payoff, and thus not maximize the money you receive.\n\n\nPress ‘enter’ to continue.',
    pos = (0,0),
    color=[1,1,1],
    height=40,
    wrapWidth=scrnsize[0]*.75
    )

stratInst3 = visual.TextStim(
    win,
    text='For each decision in this round, focus on the monetary values on the screen, the probability of receiving each of those options, and how you feel about them. \n\nForget about the previous values, choices, and outcomes and simply focus on the current trial. \n\nIf you select the gamble, you have an equal chance of receiving either amount and if you select the safe option, that will be the outcome for that trial. \n\nThis is true regardless of what has happened earlier in the task. \n\n\nPress ‘enter’ to continue.',
    pos = (0,0),
    color=[1,1,1],
    height=40,
    wrapWidth=scrnsize[0]*.75
    )

stratInst4 = visual.TextStim(
    win,
    text='Remember that you will be paid the outcome of one randomly selected trial.\n\n On each trial, think about how you would feel if the outcome on this trial was randomly selected as your cash payment.\n\nFor this round, approach the task and evaluate your choice options with a focus on only that choice, in isolation from any context.\n\n\nPress ‘enter’ to continue.',
    pos = (0,0),
    color=[1,1,1],
    height=40,
    wrapWidth=scrnsize[0]*.75
    )

strategyReminder1  = visual.TextStim(
    win,
    text='As a reminder, in this round of the task, please make your choices in isolation from any context, considering each choice solely on its own merits.\n\nOn each trial, focus on the monetary values on the screen, the probability of receiving each of those options, and how you feel about them.\n\n\nPress ‘enter’ to continue.',
    pos = (0,0),
    color=[1,1,1],
    height=40,
    wrapWidth=scrnsize[0]*.75
    )

strategyReminder2 = visual.TextStim(
    win,
    text='Forget about the previous values, choices, and outcomes and simply focus on the current trial.\n\nThink about how you would feel if the outcome on this trial was randomly selected as your cash payment.\n\nFor this round, approach the task and evaluate your choice options with a focus on only that choice, in isolation from any context.\n\n\nPress ‘enter’ to continue.',
    pos = (0,0),
    color=[1,1,1],
    height=40,
    wrapWidth=scrnsize[0]*.75
    )




summarizeInst = visual.TextStim(
    win,
    text='Let the experimenter know that you are done reading the instructions.',
    pos = (0,0),
    color=[1,1,1],
    height=40,
    wrapWidth=scrnsize[0]*.75
    )

startTaskRound1 = visual.TextStim(
    win, 
    text='The experimenter will now leave the room.\n\n Once the experimenter leaves the room, you may begin ROUND 1 of the gambling task. \n\n Press "V" or "N" to begin the task.', 
    pos = (0,0),
    color=[1,1,1],
    height = 40,
    wrapWidth = scrnsize[0]*.75
    )


startTaskRound2 = visual.TextStim(
    win, 
    text='The experimenter will now leave the room.\n\n Once the experimenter leaves the room, you may begin ROUND 2 of the gambling task. \n\n Press "V" or "N" to begin the task.', 
    pos = (0,0),
    color=[1,1,1],
    height = 40,
    wrapWidth = scrnsize[0]*.75
    )

postTask1 = visual.TextStim(
    win, 
    text='ROUND 1 of the task is complete! \n\nRandomly selecting outcome...', 
    pos = (0,0),
    color=[1,1,1],
    height = 40,
    wrapWidth = scrnsize[0]*.75
    )

postTask2 = visual.TextStim(
    win, 
    text='ROUND 2 of the task is complete! \n\nRandomly selecting outcome...', 
    pos = (0,0),
    color=[1,1,1],
    height = 40,
    wrapWidth = scrnsize[0]*.75
    )

ocSelect = visual.TextStim(
    win,  
    pos = (0,0),
    color=[1,1,1],
    height =40,
    wrapWidth = scrnsize[0]*.75
    )

#GET STIMULI READY FOR ENTIRE TASK
# prep stuff for choice display
circle = visual.Circle(
    win=win,
    units="pix",
    radius=radius,
    fillColor=[1, 1, 1],
    lineColor=[1, 1, 1],
    edges =128 #make the circle smoother
)


# text for v and n choice buttons:
vTxt = visual.TextStim(
    win=win,
    text='V - Left',
    color = [1,1,1],
    font='Helvetica',
    pos=[centerL[0],100-radius*1.5],
    height =textHeight/2
)


nTxt = visual.TextStim(
    win=win,
    text='N - Right',
    color = [1,1,1],
    font='Helvetica',
    pos=[centerR[0],100-radius*1.5],
    height =textHeight/2
)

#draw a line that will intersect the gamble circle:
line = visual.Line( 
    win = win,
    units="pix",
    lineColor = [-1,-1,-1]
)

#set up text format for $ amounts, text and position will vary each trial:
gainTxt = visual.TextStim(
    win=win,
    color = [-1,-1,-1],
    font='Helvetica',
    height =textHeight
)

lossTxt = visual.TextStim(
    win=win,
    color = [-1,-1,-1],
    font='Helvetica',
    height =textHeight
)

altTxt = visual.TextStim(
    win=win,
    color = [-1,-1,-1],
    font='Helvetica',
    height =textHeight
)

orTxt = visual.TextStim(
    win=win,
    text="OR",
    pos=center,
    color = [1,1,1],
    font='Helvetica',
    height =textHeight/2
)

#ISI STIMULI (iti will use same stimuli):
isiStim = visual.Circle(
    win=win,
    units="pix",
    radius=1,
    fillColor=[1, 1, 1],
    lineColor=[1, 1, 1],
    edges =128 #make the circle smoother
)

itiStim = isiStim

# OUTCOME stimuli
noRespTxt = visual.TextStim(
    win=win,
    text='You did not respond in time...',
    color = [1,1,1],
    font='Helvetica',
    pos=center,
    height =textHeight/2,
    wrapWidth = scrnsize[0]*.75
)

#black rectangles to cover up half the circle during outcome period, position will vary
rect4win = visual.Rect( 
    win=win,
    units="pix",
    width=rectWidth,
    height=rectHeight,
    fillColor=[-1, -1, -1],
    lineColor=[-1, -1, -1],
)

rect4loss = visual.Rect( 
    win=win,
    units="pix",
    width=rectWidth,
    height=rectHeight,
    fillColor=[-1, -1, -1],
    lineColor=[-1, -1, -1],
)

ocCircle = visual.Circle(
    win=win,
    units="pix",
    radius=radius,
    fillColor=[1, 1, 1],
    lineColor=[1, 1, 1],
    edges =128 #make the circle smoother
)

# progress bars
# this is the dimension where the progres bar starts
progBarStart = [scrnsize[1]*-.45,scrnsize[1]*-.375]
progBarEnd = [progBarStart[0]+5,progBarStart[1]]

progBarWht = visual.Line(win, start=progBarStart, end=progBarEnd, units='pix', lineWidth=textHeight/6, lineColor='white')
progBarGrn = visual.Line(win, start=progBarStart, end=progBarEnd, units='pix', lineWidth=textHeight/6, lineColor=[0,.6,0])
progBarPrpl = visual.Line(win, start=progBarStart, end=progBarEnd, units='pix', lineWidth=textHeight/6, lineColor=[.5,0,.5])

#progBar = visual.Line(win, start=[-300,-300], end=[-295,-300], units='pix', lineWidth=10, lineColor=[0,.6,0])

# these dimensions are where the progress bar ends when task is done
#progBar = visual.Line(win, start=[scrnsize[1]*-.375,scrnsize[1]*-.375], end=[scrnsize[1]*.375,scrnsize[1]*-.375], units='pix', lineWidth=textHeight/7, lineColor=[0,.6,0])
#progBar = visual.Line(win, start=[-300,-300], end=[300,-300], units='pix', lineWidth=10, lineColor=[0,.6,0])

progBarOutline = visual.Rect(win, width=((progBarStart[0]*-1)+10)*2, height=textHeight/5, units='pix', pos=[center[0],progBarStart[1]], lineColor = "white", fillColor=None)
#progBarOutline = visual.Rect(win, width=600, height=12, units='pix', pos=[center[0],-300], lineColor = "white")

#POST TASK QUESTIONS STIMULI
postQPrompt= visual.TextStim(
    win, 
    pos = (0,0),
    color=[1,1,1],
    height = 40,
    wrapWidth = scrnsize[0]*.75
)


# ---- START INSTRUCTIONS + PRACTICE ---- #
mes1.draw()
win.flip()
core.wait(1)

mes2.draw()
win.flip()
event.waitKeys(keyList = ['space'], timeStamped = False) # waiting for key press or until max time allowed

inst1.draw()
win.flip()
event.waitKeys(keyList = ['space'], timeStamped = False) # waiting for key press or until max time allowed

inst2.draw()
win.flip()
event.waitKeys(keyList = ['space'], timeStamped = False) # waiting for key press or until max time allowed

inst3.draw()
win.flip()
event.waitKeys(keyList = ['v', 'n'], timeStamped = False) # waiting for key press or until max time allowed


#------------------PRACTICE TRIALS-----------------#

# Participants do the practice trials once.

nPract=3 # number of practice trials
itiPract = 1, 1.5, 1, 2, 1 

#practice values (same for all participants):
gainPract = 53.17,6.45, 28.16, 8.50,30.54
lossPract =0,0,0,0,0
safePract = 27.89,5.10,17.05,4.12,17.25



practiceData = [] # create data structure with column names
practiceData.append(
    [
        "riskyGain", 
        "riskyLoss", 
        "safe", 
        "RT", 
        "loc", 
        "response", 
        "choice",
        "outcome",
        "iti",
        #"itiExtra",
        "stimDispStart",
        "choiceTimeStart",
        "isiStart",
        "outcomeDispStart",
        "itiStart",
        "trial"
    ]
)
    
# some set up for progress bar
percentComplete = 0 # empty object for the loop
progressTxt = visual.TextStim(win) 
#progressTxt.text = text= "%d %% complete" % percentComplete
progressTxt.text = text= "Trial %d/%d " % (0,nPract)
progressTxt.color = 'white'
progressTxt.pos = [progBarStart[0]+25,-360]
progressTxt.height = textHeight/5



changeInBar = int((progBarStart[0]/nPract)*-1)*2 # double it because it needs to go across the entire screen (not just half)


pracStart = core.Clock() # starts clock for practice 
#pracStart.reset() # resets the clock
    
for p in range(nPract):
    
    t = p+1 # to make t (trial) = 1 since python starts at 0


    
    progBarWht.end += [changeInBar,00]
    percentComplete = t/nPract *100
    #progressTxt.text = text= "%d %% complete" % percentComplete
    progressTxt.text = text= "Trial %d/%d " % (t,nPract)
    
    progressTxt.draw() # draws the message to the window, but only during the loop
    progBarOutline.draw()
    progBarWht.draw()

    gainTxt.text = text='$%.2f' % gainPract[p]
    lossTxt.text = text='$%d' % lossPract[p]
    altTxt.text = text='$%.2f' % safePract[p]

# randomly choose location of gamble on screen
    loc = random.choice([1,2]) 
#loc = 1; gamble on left, alt on right
#loc = 2; gamble on the right, alt on left




    if loc == 1:
        lnstart=lnGamL[0]
        lnend= lnGamL[1]
        gainpos= gainGamL
        losspos = lossGamL
        altpos=altGamL
        rectGainPos = [centerL[0], centerL[1]+(radius*.5)]
        rectLossPos = [centerL[0], centerL[1]-(radius*.5)]
    elif loc == 2:
        lnstart=lnGamR[0]
        lnend= lnGamR[1]
        gainpos= gainGamR
        losspos = lossGamR
        altpos=altGamR
        rectGainPos = [centerR[0], centerR[1]+(radius*.5)]
        rectLossPos = [centerR[0], centerR[1]-(radius*.5)]



#now that we know the location of gamble, where will the text go?:
    gainTxt.pos = gainpos
    lossTxt.pos = losspos
    altTxt.pos = altpos

# set line start and finish based on loc settings
    line.start=[lnstart,100]
    line.end = [lnend,100]
    line.lineWidth= 5

#draw the stuff

    #while pracStart.getTime() < t*(stimTime) + p*(choiceTime + outcomeTime + isi) + sum(itiPract[0:t]):

    for side in [-1, 1]:
        circle.pos= [centerL[0]*side,100]
        circle.draw() #draw two circles
    line.draw()
    orTxt.draw()
    altTxt.draw()
    gainTxt.draw()
    lossTxt.draw()
    win.flip() #show the choice options, keep stimuli on the screen
    stimDispStart = pracStart.getTime()
    core.wait(stimTime)

    #while pracStart.getTime() < t*(stimTime+choiceTime) + p*(outcomeTime + isi) + sum(itiPract[0:t]):

    progressTxt.draw() # draws the message to the window, but only during the loop
    progBarOutline.draw()
    progBarWht.draw()        

    # draw stimuli again with v and n displayed
    for side in [-1, 1]:
        circle.pos= [centerL[0]*side,100]
        circle.draw() #draw two circles
    line.draw()
    orTxt.draw()
    altTxt.draw()
    gainTxt.draw()
    lossTxt.draw()
    vTxt.draw()
    nTxt.draw()
    win.flip() #show the choice options
    choiceTimeStart = pracStart.getTime()

    rtClock=core.Clock() #start the clock and wait for a response
    response = event.waitKeys(maxWait = choiceTime, keyList = ['v', 'n'], timeStamped = False) # waiting for key press or until max time allowed
    #response = event.waitKeys(keyList = ['v', 'n'], timeStamped = False) # waiting for key press or until max time allowed
    if response is None:
        RT = 'NaN'
        #itiExtra = 0
    elif ['v'] or ['n'] in response:
        RT=rtClock.getTime()
        #itiExtra = choiceTime-RT # time that gets added on to the end of the trial


    # record what their choice is based on response and location of gamble on screen
    if loc == 1 and response == ['v'] or loc ==2 and response == ['n']: #they gambled
        choice = 1
        outcome = random.choice([gainPract[p],lossPract[p]])
    elif loc==1 and response == ['n'] or loc==2 and response ==['v']: #they took safe
        choice = 0
        outcome = safePract[p]
    else:
        choice = 'NaN'
        outcome = 'NaN' 

    if outcome == gainPract[p]:
        rect = rect4win
        rect.pos = rectLossPos
        ocCircle.pos = [gainpos[0],100] #draw the circle on the side where gamble was displayed
        ocTxt = gainTxt
    elif outcome == lossPract[p]:
        rect = rect4loss
        rect.pos= rectGainPos
        ocCircle.pos = [gainpos[0],100] # draw the circle on the side where gamble was displayed
        ocTxt = lossTxt
    elif outcome == safePract[p]:
        ocCircle.pos = [altpos[0],100] #draw circle on the side that safe option was displayed
        ocTxt = altTxt







    #DO THE ISI
    
    progressTxt.draw() # draws the message to the window, but only during the loop
    progBarOutline.draw()
    progBarWht.draw()   
    
    isiStim.draw()
    win.flip() # show it
    isiStart = pracStart.getTime()
    core.wait(isi)

    #DO THE OUTCOME
    if outcome == 'NaN':
        ocTxt = noRespTxt
    else:
        ocCircle.draw()
        ocTxt.draw()
        if outcome == gainPract[p] or outcome == lossPract[p]:
            rect.draw()

    progressTxt.draw() # draws the message to the window, but only during the loop
    progBarOutline.draw()
    progBarWht.draw()   
    ocTxt.draw()
    win.flip() # show it
    outcomeDispStart = pracStart.getTime()
    core.wait(outcomeTime)

    #ITI    
    itiStart = pracStart.getTime()
    while pracStart.getTime() < t*(stimTime + choiceTime + isi + outcomeTime) + sum(itiPract[0:t]):
        
        progressTxt.draw() # draws the message to the window, but only during the loop
        progBarOutline.draw()
        progBarWht.draw()   
        itiStim.draw()
        win.flip()
        
    
    # save data on a trial by trial basis
    practiceData.append(
        [
            gainPract[p], 
            lossPract[p], 
            safePract[p], 
            RT, 
            loc, 
            response, 
            choice,
            outcome,
            itiPract[p],
            #itiExtra,
            stimDispStart,
            choiceTimeStart,
            isiStart,
            outcomeDispStart,
            itiStart,
            t
        ]
    )


postPrac.draw()
win.flip()
event.waitKeys(keyList = ['space'], timeStamped = False) # waiting for key press or until max time allowed

#win.close() # for testing just the practice trials

practiceData = pd.DataFrame(practiceData)


# save practice file
datetime = time.strftime("%Y%m%d-%H%M%S"); # save date and time
filename = "rcsRDMpractice_" + "sub" + subID + "_" + datetime + ".csv"; # make filename
practiceData.to_csv(filename)


#----------Start the task---------#
try:

    data = [] # create data structure with column names
    data.append(
        [
            "subID",
            "riskyGain", 
            "riskyLoss", 
            "safe", 
            "RT", 
            "loc", 
            "response", 
            "choice",
            "outcome",
            "iti",
            "evLevel",
            "evInd",
            "runSize",
            "strategy",
            "stimDispStart",
            "choiceTimeStart",
            "isiStart",
            "outcomeDispStart",
            "itiStart",
            "trial",
            "roundRDM"
        ]
    )
    
    # some set up for progress bar
    #progressTxt = visual.TextStim(win) 
    progressTxt.text = text= "Trial %d/%d " % (0,nPract)
    #progressTxt.color = 'white'
    #progressTxt.pos = [progBarStart[0]+25,-360]
    #progressTxt.height = textHeight/5  


    changeInBar = int((progBarStart[0]/nT)*-1)*2 # double it because it needs to go across the entire screen (not just half)


    
    
    for r in range(RDMrounds):
        
        

        
        #reset the progress bars before each round
        progBarGrn = visual.Line(win, start=progBarStart, end=progBarEnd, units='pix', lineWidth=textHeight/6, lineColor=[0,.6,0])
        progBarPrpl = visual.Line(win, start=progBarStart, end=progBarEnd, units='pix', lineWidth=textHeight/6, lineColor=[.5,0,.5])

         
        # which progress bar and outline will we show?
        if colorOrder[r] == 0:
            progBarReal = progBarGrn
            borderBox = greenBox
        elif colorOrder[r] ==1:
            progBarReal = progBarPrpl
            borderBox = purpleBox
                        
        
        # generate the choiceset on each round
        rcsCS = rcsRDMChoiceSet()  
    
       
        # store some of the choice set features in new variables
        riskyGain = rcsCS['riskyGain']
        riskyLoss = rcsCS['riskyLoss']
        safe = rcsCS['alternative']
        evLevel = rcsCS['evLevel']
        evInd = rcsCS['evInd']
        runSize = rcsCS['runSize']
    
    
    
        #ITIs change as a function of choiceset
        iti = rcsCS['iti']
    
    

        # set up border color
        borderBox.draw() # draw the large color box
        blackBox.draw() # draw smaller black box on top of our color rect to create border effect

        """
        Depending on round and whether participant is switching, we will show 
        slightly different instructions. 
        
        If its round 1, participants will read the full
        instructions for the assigned condition. 
        
        If its round 2 and the participant is switching conditions, 
        they will read a screen that tells them they will be reading new 
        instructions, then they will read the new instructions in their entirety.
        
        If its round 2 and the participant is repeating conditions, participants
        will be told they will read a reminder and then they will read the reminder 
        instructions.
        
        All participants will be asked to summarize the instructions no matter the round
        or condition or switching/repeating.
        """

        # the first screen in the series of instructions gives the participant a heads up 
        # that instructions are coming up.
        if r == 0:
            prepForConditionRound1.draw() #"Before we begin ROUND 1..."
            # this is the same for all participants, just one screen
        elif r==1 and cond[r] == cond[r-1]: # if we are in the second round and participant is repeating conditions
            prepForConditionRound2_pg1Repeating.draw() #"Before we begin ROUND 2..." first page of instructions in round 1
        elif r==1 and cond[r] != cond[r-1]: # if we are in the second round and participant is switching conditions
            prepForConditionRound2_pg1Switching.draw() 
            
        win.flip()
        event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press
        
        if r==1: # round 2 has a second page of prep instructions
            # set up border color
            borderBox.draw() # draw the large color box
            blackBox.draw() # draw smaller black box on top of our color rect to create border effect
            
            # draw and show page 2, wait for response
            prepForConditionRound2_pg2forAllSubs.draw()
            win.flip()
            event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press

    # Determine the condition specific instructions    
        strategy = cond[r]; # store strategy value (0/1)   
        
        if r == 0 or r==1 and strategy!=cond[r-1]: # round 1 or switiching in round 2, we show the full control or strategy instructions

            if strategy == 0: # if the condition is control
                instructPG1 = controlInst1
                instructPG2 = controlInst2
                instructPG3 = controlInst3
                instructPG4 = controlInst4
                
            elif strategy == 1: # if the condition is strategy
                instructPG1 = stratInst1
                instructPG2 = stratInst2
                instructPG3 = stratInst3
                instructPG4 = stratInst4

                
            #show page 1
            borderBox.draw() # draw the large color box
            blackBox.draw() # draw smaller black box on top of our color rect to create border effect
            
            instructPG1.draw()
            win.flip()
            event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press 
            
            #show page 2
            borderBox.draw() # draw the large color box
            blackBox.draw() # draw smaller black box on top of our color rect to create border effect
            
            instructPG2.draw()
            win.flip()
            event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press 
            
            #show page 3
            borderBox.draw() # draw the large color box
            blackBox.draw() # draw smaller black box on top of our color rect to create border effect
            
            instructPG3.draw()
            win.flip()
            event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press 
            
            #show page 4
            borderBox.draw() # draw the large color box
            blackBox.draw() # draw smaller black box on top of our color rect to create border effect
            
            instructPG4.draw()
            win.flip()
            event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press 
        
        elif r==1 and strategy==cond[r-1]: # if round 2 and repeting condition (two instead of 4 pages)
            if  strategy ==0: # if control condition
                instructPG1 = controlReminder1
                instructPG2 = controlReminder2
                
            elif strategy ==1: # if strategy condition
                instructPG1 = strategyReminder1
                instructPG2 = strategyReminder2

            #show page 1
            borderBox.draw() # draw the large color box
            blackBox.draw() # draw smaller black box on top of our color rect to create border effect
             
            instructPG1.draw()
            win.flip()
            event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press 
             
            #show page 2
            borderBox.draw() # draw the large color box
            blackBox.draw() # draw smaller black box on top of our color rect to create border effect
             
            instructPG2.draw()
            win.flip()
            event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press 
 


        # Now the rest is mostly the same for all participants/conditions/switching show the summarize prompt
        borderBox.draw() # draw the large color box
        blackBox.draw() # draw smaller black box on top of our color rect to create border effect
        
        summarizeInst.draw()
        win.flip()
        event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press
        
        
        borderBox.draw() # draw the large color box
        blackBox.draw() # draw smaller black box on top of our color rect to create border effect
        
        # depending on round of task, show slightly different start screen
        if r==0:
            startTaskRound1.draw()
        elif r==1:
            startTaskRound2.draw()
            
        win.flip()
        event.waitKeys(keyList = ['v', 'n'], timeStamped = False) # waiting for key press or until max time allowed
        # experimenter leaves the room, participant starts round 1 of the study
        
        rdmStart = core.Clock() # starts clock for rdm task 

        for t in range(nT):
            

            s = t+1 # new counter that starts at 1 since python starts at 0

                        
            progBarReal.end += [changeInBar,00]
            progressTxt.text = text= "Trial %d/%d " % (s,nT)
            
            
            gainTxt.text = text='$%.2f' % riskyGain[t]
            lossTxt.text = text='$%d' % riskyLoss[t]
            altTxt.text = text='$%.2f' % safe[t]
        
        # randomly choose location of gamble on screen
            loc = random.choice([1,2]) 
        #loc = 1; gamble on left, alt on right
        #loc =2; gamble on the right, alt on left
            
            if loc == 1:
                lnstart=lnGamL[0]
                lnend= lnGamL[1]
                gainpos= gainGamL
                losspos = lossGamL
                altpos=altGamL
                rectGainPos = [centerL[0], centerL[1]+(radius*.5)]
                rectLossPos = [centerL[0], centerL[1]-(radius*.5)]
            elif loc == 2:
                lnstart=lnGamR[0]
                lnend= lnGamR[1]
                gainpos= gainGamR
                losspos = lossGamR
                altpos=altGamR
                rectGainPos = [centerR[0], centerR[1]+(radius*.5)]
                rectLossPos = [centerR[0], centerR[1]-(radius*.5)]
        
        
        
        #now that we know the location of gamble, where will the text go?:
            gainTxt.pos = gainpos
            lossTxt.pos = losspos
            altTxt.pos = altpos
        
        # set line start and finish based on loc settings
            line.start=[lnstart,100]
            line.end = [lnend,100]
            line.lineWidth= 5
        
        #draw the stuff
            borderBox.draw() # draw the large color box
            blackBox.draw() # draw smaller black box on top of our color rect to create border effect
            progressTxt.draw() # draws the message to the window, but only during the loop
            progBarOutline.draw()
            progBarReal.draw()
            
        
            for side in [-1, 1]:
                circle.pos= [centerL[0]*side,100]
                circle.draw() #draw two circles
            line.draw()
            orTxt.draw()
            altTxt.draw()
            gainTxt.draw()
            lossTxt.draw()
            win.flip() #show the choice options, keep stimuli on the screen
            stimDispStart = rdmStart.getTime()
            core.wait(stimTime)
        
        # draw stuff again with "v" and "n"
            borderBox.draw() # draw the large color box
            blackBox.draw() # draw smaller black box on top of our color rect to create border effect
            progressTxt.draw() # draws the message to the window, but only during the loop
            progBarOutline.draw()
            progBarReal.draw()
            
            for side in [-1, 1]:
                circle.pos= [centerL[0]*side,100]
                circle.draw() #draw two circles
            line.draw()
            orTxt.draw()
            altTxt.draw()
            gainTxt.draw()
            lossTxt.draw()
            vTxt.draw()
            nTxt.draw()
            win.flip(choiceTime) #show the choice options
            choiceTimeStart = rdmStart.getTime()

            clock=core.Clock() #start the clock and wait for a response
            response = event.waitKeys(maxWait = stimTime, keyList = ['v', 'n'], timeStamped = False) # waiting for key press or until max time allowed
            if response is None:
                RT = 'NaN'
            elif ['v'] or ['n'] in response:
                RT=clock.getTime()
        
            # record what their choice is based on response and location of gamble on screen
            if loc == 1 and response == ['v'] or loc ==2 and response == ['n']: #they gambled
                choice = 1
                outcome = random.choice([riskyGain[t],riskyLoss[t]])
            elif loc==1 and response == ['n'] or loc==2 and response ==['v']: #they took safe
                choice = 0
                outcome = safe[t]
            else:
                choice = 'NaN'
                outcome = 'NaN' 
        
            if outcome == riskyGain[t]:
                rect = rect4win
                rect.pos = rectLossPos
                ocCircle.pos = [gainpos[0],100] #draw the circle on the side where gamble was displayed
                ocTxt = gainTxt
            elif outcome == riskyLoss[t]:
                rect = rect4loss
                rect.pos= rectGainPos
                ocCircle.pos = [gainpos[0],100] # draw the circle on the side where gamble was displayed
                ocTxt = lossTxt
            elif outcome == safe[t]:
                ocCircle.pos = [altpos[0],100] #draw circle on the side that safe option was displayed
                ocTxt = altTxt
        
        
            #DO THE ISI
            borderBox.draw() # draw the large color box
            blackBox.draw() # draw smaller black box on top of our color rect to create border effect
            progressTxt.draw() # draws the message to the window, but only during the loop
            progBarOutline.draw()
            progBarReal.draw()
            
            isiStim.draw()
            win.flip() # show it
            isiStart = rdmStart.getTime()
            core.wait(isi)
        
            #DO THE OUTCOME
            borderBox.draw() # draw the large color box
            blackBox.draw() # draw smaller black box on top of our color rect to create border effect
            progressTxt.draw() # draws the message to the window, but only during the loop
            progBarOutline.draw()
            progBarReal.draw()
            
            if outcome == 'NaN':
                ocTxt = noRespTxt
            else:
                ocCircle.draw()
                ocTxt.draw()
                if outcome == riskyGain[t] or outcome == riskyLoss[t]:
                    rect.draw()
        
            ocTxt.draw()
            win.flip() # show it
            outcomeDispStart = rdmStart.getTime()
            core.wait(outcomeTime)
        
            #ITI 
            itiStart = rdmStart.getTime()
            while rdmStart.getTime() < s*(stimTime + choiceTime + isi + outcomeTime) + sum(iti[0:s]):
                borderBox.draw() # draw the large color box
                blackBox.draw() # draw smaller black box on top of our color rect to create border effect
                progressTxt.draw() # draws the message to the window, but only during the loop
                progBarOutline.draw()
                progBarReal.draw()
                itiStim.draw()
                win.flip()
                #core.wait(iti[t])
            

        
        # save data on a trial by trial basis
            data.append(
                [
                    subID,
                    riskyGain[t], 
                    riskyLoss[t], 
                    safe[t], 
                    RT, 
                    loc, 
                    response, 
                    choice,
                    outcome,
                    iti[t],
                    evLevel[t],
                    evInd[t],
                    runSize[t],
                    cond[r],
                    stimDispStart,
                    choiceTimeStart,
                    isiStart,
                    outcomeDispStart,
                    itiStart,
                    s,
                    r+1
                ]
            )
            
                
        
        
        datatopickoutcomes = pd.DataFrame(data[1:len(data)], columns = data[0]) # convert to dataframe
        datatopickoutcomes = datatopickoutcomes.loc[datatopickoutcomes['roundRDM'] == (r+1)]; # just want the one round
        allOutcomes = datatopickoutcomes['outcome'] # save just the outcomes
        
        # select an outcome to pay participant
        #realOutcomes = allOutcomes[allOutcomes != 'NaN']
        realOutcomes = datatopickoutcomes[allOutcomes != 'NaN'] #NEED TO DOUBLE CHECK THAT THIS INDEXES CORRECTLY WHEN THERE ARE NANS
  
    
        trialChosen = np.random.choice(realOutcomes['trial']) # randomly select a trial
        ocChosen = realOutcomes['outcome'][realOutcomes['trial']==trialChosen] # pull out outcome based on randomly selected trial
            
        data.append([ocChosen])
        
        
        borderBox.draw() # draw the large color box
        blackBox.draw() # draw smaller black box on top of our color rect to create border effect
        
        if r ==0:
            postTask1.draw() #"randomly selecting outcome..."
        elif r==1:
            postTask2.draw()
        win.flip()
        core.wait(2)
    
        
        if r==0:
            ocSelect.text= text='For ROUND 1, trial %d was randomly selected and the outcome on that trial was $%.2f. \n\nThis outcome will be one of the two outcomes randomly selected for payment at the end of the next round of the task. \n\nYou will now be asked two questions about your experience in the task. \n\nPress ‘enter’ to continue.' % (trialChosen, ocChosen)
        elif r==1:
            ocSelect.text= text='For ROUND 2, trial %d was randomly selected and the outcome on that trial was $%.2f. \n\nThis outcome will be one of the two outcomes randomly selected for payment. \n\nYou will now be asked two questions about your experience in the task. \n\nPress ‘enter’ to continue.' % (trialChosen, ocChosen)
        
        borderBox.draw() # draw the large color box
        blackBox.draw() # draw smaller black box on top of our color rect to create border effect
        ocSelect.draw() #"You will receive ..."
        win.flip()
        event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press 
        
        
        # 2 post-task questions
        if strategy ==0: # control condition
            postQPrompt.text=text="For ROUND %d, you were asked to behave naturally..." % r+1
 
        elif strategy ==1:
            postQPrompt.text=text="For ROUND %d, you were asked to ignore context..." % r+1
            
             
        borderBox.draw() # draw the large color box
        blackBox.draw() # draw smaller black box on top of our color rect to create border effect
        postQPrompt.draw() 
        win.flip()
        event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press 
        

finally: # this should save the data even if something in "try" fails
    win.close()
    data = pd.DataFrame(data)
    

    # save file
    datetime = time.strftime("%Y%m%d-%H%M%S"); # save date and time
    filename = "rcsRDM_" + "sub" + subID + "_" + datetime + ".csv"; # make filename
    data.to_csv(filename)









