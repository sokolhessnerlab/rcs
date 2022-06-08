#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 14:26:15 2022

@author: hayley
"""


"""
Risky decision-making for HRB dissertation project: Risk, context and strategy. 
"""

#def rcsRDM(subID, cond1, cond2):
subID='001'
cond1 = 0
cond2 = 1
    

# IMPORT STUFF
import random, time, pandas as pd
from psychopy import visual, core, event
import numpy as np


# get the choice set function
from rcsRDMChoiceSet import *


# set up file name
datetime = time.strftime("%Y%m%d-%H%M%S"); # save date and time
filename = "rcsRDM_" + "sub" + subID + "_" + datetime + ".csv"; # make filename

RDMrounds=2;


cond = [cond1, cond2];
  
# generate the choicesets
rcsCS = rcsRDMChoiceSet()  # round 1




riskyGain = rcsCS['riskyGain']
riskyLoss = rcsCS['riskyLoss']
safe = rcsCS['alternative']
evLevel = rcsCS['evLevel']
evInd = rcsCS['evInd']
runSize = rcsCS['runSize']


#SET UP SCREEN DIMENSIONS N STUFF
scrnsize= [800,800] #how large the screen will be
center = [0,0]
centerR = [scrnsize[0]/4,0]
centerL = [scrnsize[0]/-4,0]
radius = scrnsize[0]/5.5
rectHeight = radius +2 #rectangle used to cover up half the circle when outcome is gain or loss
rectWidth = radius*2+2
textHeight = radius/2
nT = 5 #for testing purposes
#nT = len(safe) # for real

#TIMING STUFF
stimTime = 4
isi = rcsCS['isi']
outcomeTime =1
iti = rcsCS['iti']


#where to draw line and dollar amounts:

lnGamL =[centerL[0]-radius-2, centerL[0]+radius+2] #x start and end points for line when gamble is on the left
lnGamR = [centerR[0]-radius-2, centerR[0]+radius+2] # x start and end points for line when gamble is on the right

gainGamL = [centerL[0], centerL[1]+(radius*.5)] #position of gain amount when gamble on the left
gainGamR = [centerR[0], centerR[1]+(radius*.5)] #position of gain amount when gamble on the right

lossGamL= [centerL[0], centerL[1]-(radius*.5)] #position of loss amount when gamble on the left
lossGamR= [centerR[0], centerR[1]-(radius*.5)] #position of loss amount when gamble on the right

altGamL = [centerR[0], 0] #position of safe amount when gamble on the left
altGamR = [centerL[0], 0] #position of safe amount when gamble on the right

# GET THE WINDOW READY - BLACK SCREEN
win = visual.Window(
    size=scrnsize,
    units="pix",
    fullscr=False,
    color=[-1, -1, -1] #black screen
)


# INSTRUCTIONS

mes1 = visual.TextStim(win, text='Setting up...', pos = (0,0),color=[1,1,1], height=40)
mes2 = visual.TextStim(win, text='Waiting for experimenter', pos = (0,0),color=[1,1,1], height =40)
inst1 = visual.TextStim(
    win, 
    text='As discussed, in this task you will choose between a gamble and a guaranteed alternative. \n\nPress "V" to choose the left option and "N" to choose the right option.\n\nYou will have 4 seconds to respond.', 
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

controlInst = visual.TextStim(
    win,
    text='You will now read these additional instructions about behaving naturally before doing this task. When you are ready to proceed, press enter.',
    pos = (0,0),
    color=[1,1,1],
    height=40,
    wrapWidth=scrnsize[0]*.75
    )


stratInst = visual.TextStim(
    win,
    text='You will now read these additional instructions about ignoring context before doing this task. When you are ready to proceed, press enter.',
    pos = (0,0),
    color=[1,1,1],
    height=40,
    wrapWidth=scrnsize[0]*.75
    )

summarizeInst = visual.TextStim(
    win,
    text='Please provide a very brief (1 sentence) verbal summary to the experimenter about the instructions you just read.',
    pos = (0,0),
    color=[1,1,1],
    height=40,
    wrapWidth=scrnsize[0]*.75
    )

startTask = visual.TextStim(
    win, 
    text='The experimenter will now leave the room.\n\nPress "V" or "N" when you are ready to begin the task.', 
    pos = (0,0),
    color=[1,1,1],
    height = 40,
    wrapWidth = scrnsize[0]*.75
    )

postTask = visual.TextStim(
    win, 
    text='Task complete! \n\nRandomly selecting outcome...', 
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
    text='V',
    color = [1,1,1],
    font='Helvetica',
    pos=[centerL[0],0-radius*1.5],
    height =textHeight
)

nTxt = visual.TextStim(
    win=win,
    text='N',
    color = [1,1,1],
    font='Helvetica',
    pos=[centerR[0],0-radius*1.5],
    height =textHeight
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

#ISI STIMULI (iti will use same stimuli):
isiStim = visual.Circle(
    win=win,
    units="pix",
    radius=1,
    fillColor=[1, 1, 1],
    lineColor=[1, 1, 1],
    edges =128 #make the circle smoother
)

# OUTCOME stimuli
noRespTxt = visual.TextStim(
    win=win,
    text='You did not respond in time...',
    color = [1,1,1],
    font='Helvetica',
    pos=center,
    height =textHeight,
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

# ---- START INSTRUCTIONS + PRACTICE ---- #
mes1.draw()
win.flip()
core.wait(1)

mes2.draw()
win.flip()
event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press or until max time allowed

inst1.draw()
win.flip()
event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press or until max time allowed

inst2.draw()
win.flip()
event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press or until max time allowed

inst3.draw()
win.flip()
event.waitKeys(keyList = ['v', 'n'], timeStamped = False) # waiting for key press or until max time allowed


#------------------PRACTICE TRIALS-----------------#
nPract=5
#practice values:
gainPract = 53,6.45, 28, 8.50,30
lossPract =0,0,0,0,0
safePract = 27,5,17,4,17.25

for p in range(nPract):
    gainTxt.text = text='$%d' % gainPract[p]
    lossTxt.text = text='$%d' % lossPract[p]
    altTxt.text = text='$%d' % safePract[p]

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
    elif loc == 2:
        lnstart=lnGamR[0]
        lnend= lnGamR[1]
        gainpos= gainGamR
        losspos = lossGamR
        altpos=altGamR

#now that we know the location of gamble, where will the text go?:
    gainTxt.pos = gainpos
    lossTxt.pos = losspos
    altTxt.pos = altpos

# set line start and finish based on loc settings
    line.start=[lnstart,0]
    line.end = [lnend,0]
    line.lineWidth= 5

#draw the stuff
    for side in [-1, 1]:
        circle.pos= [centerL[0]*side,0]
        circle.draw() #draw two circles
    line.draw()
    altTxt.draw()
    gainTxt.draw()
    lossTxt.draw()
    vTxt.draw()
    nTxt.draw()
    win.flip() #show the choice options

    clock=core.Clock() #start the clock and wait for a response
    response = event.waitKeys(maxWait = stimTime, keyList = ['v', 'n'], timeStamped = False) # waiting for key press or until max time allowed
    if response is None:
        RT = 'NaN'
    elif ['v'] or ['n'] in response:
        RT=clock.getTime()

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
        rect.pos = losspos
        ocCircle.pos = [gainpos[0],0] #draw the circle on the side where gamble was displayed
        ocTxt = gainTxt
    elif outcome == lossPract[p]:
        rect = rect4loss
        rect.pos= gainpos
        ocCircle.pos = [gainpos[0],0] # draw the circle on the side where gamble was displayed
        ocTxt = lossTxt
    elif outcome == safePract[p]:
        ocCircle.pos = [altpos[0],0] #draw circle on the side that safe option was displayed
        ocTxt = altTxt


    #DO THE ISI
    isiStim.draw()
    win.flip() # show it
    core.wait(isi[p])

    #DO THE OUTCOME
    if outcome == 'NaN':
        ocTxt = noRespTxt
    else:
        ocCircle.draw()
        ocTxt.draw()
        if outcome == gainPract[p] or outcome == lossPract[p]:
            rect.draw()

    ocTxt.draw()
    win.flip() # show it
    core.wait(outcomeTime)

    #ITI 
    itiStim = isiStim
    itiStim.draw()
    win.flip()
    core.wait(2)


postPrac.draw()
win.flip()
event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press or until max time allowed




# Condition specific instructions

# for r in range(RDMrounds):
    # if cond[r] == 0: 
        #controlInst.draw()
    #elif cond[r] ==1: 
        #stratInst.draw()
        
if cond[0] == 0: 
    controlInst.draw()
elif cond[0] ==1: 
    stratInst.draw()
    
win.flip()
event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press or until max time allowed

summarizeInst.draw()
win.flip()
event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press or until max time allowed


# create data structure
data = []
data.append(
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
        "evLevel",
        "evInd",
        "runSize"
        "strategy"
    ]
)


# ------------------------ START TASK ------------------------ # 
startTask.draw()
win.flip()
event.waitKeys(keyList = ['v', 'n'], timeStamped = False) # waiting for key press or until max time allowed


for t in range(nT):
    gainTxt.text = text='$%d' % riskyGain[t]
    lossTxt.text = text='$%d' % riskyLoss[t]
    altTxt.text = text='$%d' % safe[t]

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
    elif loc == 2:
        lnstart=lnGamR[0]
        lnend= lnGamR[1]
        gainpos= gainGamR
        losspos = lossGamR
        altpos=altGamR

#now that we know the location of gamble, where will the text go?:
    gainTxt.pos = gainpos
    lossTxt.pos = losspos
    altTxt.pos = altpos

# set line start and finish based on loc settings
    line.start=[lnstart,0]
    line.end = [lnend,0]
    line.lineWidth= 5

#draw the stuff
    for side in [-1, 1]:
        circle.pos= [centerL[0]*side,0]
        circle.draw() #draw two circles
    line.draw()
    altTxt.draw()
    gainTxt.draw()
    lossTxt.draw()
    vTxt.draw()
    nTxt.draw()
    win.flip() #show the choice options

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
        rect.pos = losspos
        ocCircle.pos = [gainpos[0],0] #draw the circle on the side where gamble was displayed
        ocTxt = gainTxt
    elif outcome == riskyLoss[t]:
        rect = rect4loss
        rect.pos= gainpos
        ocCircle.pos = [gainpos[0],0] # draw the circle on the side where gamble was displayed
        ocTxt = lossTxt
    elif outcome == safe[t]:
        ocCircle.pos = [altpos[0],0] #draw circle on the side that safe option was displayed
        ocTxt = altTxt


    #DO THE ISI
    isiStim.draw()
    win.flip() # show it
    core.wait(isi[p])

    #DO THE OUTCOME
    if outcome == 'NaN':
        ocTxt = noRespTxt
    else:
        ocCircle.draw()
        ocTxt.draw()
        if outcome == riskyGain[t] or outcome == riskyLoss[t]:
            rect.draw()

    ocTxt.draw()
    win.flip() # show it
    core.wait(outcomeTime)

    #ITI 
    itiStim = isiStim
    itiStim.draw()
    win.flip()
    core.wait(iti[t])

# save data on a trial by trial basis
    data.append(
        [
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
            cond[0] # change this to be cond[r] when for loop is going
        ]
    )

datatopickoutcomes = np.array(data,dtype=object)
# select an outcome to pay participant
allOutcomes = datatopickoutcomes[1:nT, [7]]
realOutcomes = allOutcomes[allOutcomes != 'NaN']
ocChosen = random.choice(realOutcomes)

ocSelect.text = 'Randomly selected\noutcome: $%d \n\nPress the white button to call the experimenter.' % ocChosen

postTask.draw() #"randomly selecting outcome..."
win.flip()
core.wait(2)

ocSelect.draw() #"You will receive ..."
win.flip()
event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press
win.close()

#pprint.pprint(data)

#np.savetxt(filename, data, newline = "\n", fmt="%s") #save data as a text file
data.append([ocChosen])

data = pd.DataFrame(data)

#csvfilename = "brooksFinal_" + "sub"+ subj_id + "_" + date + "_" + ".csv"
data.to_csv(filename)


