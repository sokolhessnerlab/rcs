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


def rcsRDM(subID, cond1, cond2, cond1color, cond2color, isReal):
    

    #subID='001'
    #cond1 = 0
    #cond2 = 1
    #cond1color = 0
    #cond2color = 1
    #isReal (1 = yes, 0 = testing)
    
    try:   
    
        # Import modules we need
        import random, time, os
        import pandas as pd
        from psychopy import visual, core, event, monitors
        import numpy as np
        
        # change directory
        #os.chdir('/Users/hayley/Documents/Github/rcs/rdmTask') # hb mac
        os.chdir('/Users/shlab/Documents/Github/rcs/task/rdmTask') # mahimahi
        #os.chdir('/Users/Display/Desktop/Github/rcs/rdmTask') # tofu
        
        
        dataDirectoryPath = '/Users/shlab/Documents/Github/rcs/task/data/'
        
        
        # Import the choice set function
        #from rcsRDMChoiceSet import *
        import rcsRDMChoiceSet
        
        # Define rounds of risky decision-making task
        RDMrounds=2; 
        
        # Store conditions in one structure 
        cond = [cond1, cond2] #(0= control, 1 = strategy)
        colorOrder = [cond1color, cond2color] #(green = 0, purple = 1)
          
        
        # Set up the experimental parameters that are consistent across task rounds:
        
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
        moneyTextHeight= textHeight*2
        wrap = scrnsize[0]*.9 # text wrapping
        
        
        if isReal == 1:
            nT = 131
            nPract = 5
        else:    
            nT = 2 #for testing purposes
            nPract = 2

        
        
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
        
        
        # set up stimuli to create the green and purple borders
        blackBox = visual.Rect(
            win,
            width=scrnsize[0]*.95, 
            height=scrnsize[1]*.95, 
            units='pix', 
            pos=[0,0], 
            fillColor='black'
        )
        
        borderBox = visual.Rect(
            win, 
            width=scrnsize[0], 
            height=scrnsize[1], 
            units='pix', 
            pos=[0,0], 
            fillColor=[0,.6,0] #green
        )
        
        
        # Prepare instructions and other task stimuli
        
        mes1 = visual.TextStim(
            win, 
            text='Setting up...', 
            pos = (0,0),
            color=[1,1,1], 
            height=40
        )
        
        mes2 = visual.TextStim(
            win, 
            text='Waiting for experimenter', 
            pos = (0,0),
            color=[1,1,1], 
            height =40
        )
        
        inst1 = visual.TextStim(
            win, 
            text='As discussed, in this task you will choose between a gamble and a guaranteed alternative. \n\n\n\nPress "V" to choose the left option and "N" to choose the right option.', 
            pos = (0,0),
            color=[1,1,1],
            height = textHeight,
            wrapWidth = wrap, 
            alignText="left"
        )
        
        inst2 = visual.TextStim(
            win, 
            text='Next up are 5 practice trials. \n\nWhat questions do you have for the experimenter? \n\nPlease ask the experimenter now.', 
            pos = (0,0),
            color=[1,1,1],
            height = textHeight,
            wrapWidth = wrap,
            alignText="left"
        )
        
        inst3 = visual.TextStim(
            win, 
            text='Press "V" or "N" when you are ready to begin the practice.', 
            pos = (0,0),
            color=[1,1,1],
            height = textHeight,
            wrapWidth = wrap,
            alignText="left"
        )
        
        postPrac = visual.TextStim(
            win, 
            text='Practice complete! \n\nWhat questions do you have for the experimenter? \n\nPlease ask the experimenter now.', 
            pos = (0,0),
            color=[1,1,1],
            height = textHeight,
            wrapWidth = wrap,
            alignText="left"
        )
        
        # SEPARATION THEATRICS FOR SEPARATING ROUNDS
        explainRounds = visual.TextStim(
            win, 
            text = "You are about to do two rounds of the task. \n\nThese tasks are completely separate. \n\nEach round will be marked with a different color (purple or green).\n\nTreat each round of the task as independent.\n\n\nPress 'enter' to continue.",
            pos = (0,0),
            color=[1,1,1],
            height = textHeight,
            wrapWidth = wrap,
            alignText="left"
        )
        
        
        readyForRound1 = visual.TextStim(
            win,
            text='Are you ready for ROUND 1 of the task?\n\n\n\nPress ‘enter’ to continue.',
            pos = (0,0),
            color=[1,1,1],
            height=textHeight,
            wrapWidth=wrap,
            alignText="left"
        )
        
        round2Prep = visual.TextStim(
            win,
            text='You are half way through the gambling portion of the experiment! \n\nYou will now do ROUND 2 which will be marked with a different color from the previous round.\n\nThe choice options and outcomes in ROUND 2 are not related to the previous round. \n\nTreat this round as a fresh start!\n\n\nPress ‘enter’ to continue.',
            pos = (0,0),
            color=[1,1,1],
            height=textHeight,
            wrapWidth=wrap,
            alignText="left"
        )               
        
        readyForRound2 = visual.TextStim(
            win,
            text='Are you ready for ROUND 2 of the task?\n\n\n\nPress ‘enter’ to continue.',
            pos = (0,0),
            color=[1,1,1],
            height=textHeight,
            wrapWidth=wrap,
            alignText="left"
        )
         
        startingRound1 = visual.TextStim(
            win,
            text='Setting up ROUND 1...',
            pos = (0,0),
            color=[1,1,1],
            height=textHeight,
            wrapWidth=wrap,
            alignText="left"
        )
        
        
        startingRound2 = visual.TextStim(
            win,
            text='Setting up ROUND 2...',
            pos = (0,0),
            color=[1,1,1],
            height=textHeight,
            wrapWidth=wrap,
            alignText="left"
        )
        
        #   PREPARING FOR THE FIRST ROUND INSTRUCTIONS
        prepForConditionRound1 = visual.TextStim(
            win,
            text='Before we begin ROUND 1 of the gambling task, you will be asked to read some additional task instructions.\n\nPlease pay close attention to the instructions as you read them.\n\n\n\nPress ‘enter’ to continue.',
            pos = (0,0),
            color=[1,1,1],
            height=textHeight,
            wrapWidth=wrap,
            alignText="left"
        )
        
        # Call experimenter
        callExperimenter = visual.TextStim(
            win,
            text="Please press the white button to call the experimenter back into the room to continue.",
            pos = (0,0),
            color="white",
            height = textHeight,
            wrapWidth=wrap,
            alignText="left"
        )
        
        
        # PREPARING FOR THE SECOND ROUND OF INSTRUCTIONS
        # if participant is switching conditions from round 1:
        prepForConditionRound2_pg1Switching = visual.TextStim(
            win,
            text='Before we begin ROUND 2 of the gambling task, you will be asked to read additional task instructions that are different from round 1. \n\nThe mechanics of the task will be the exact same but the instructions will ask you to think differently than you did in round 1. \n\nPlease pay close attention to the instructions as you read them.\n\nTry your best to forget the instructions from round 1 and follow these new instructions. \n\n\n\nPress ‘enter’ to continue.',
            pos = (0,0),
            color=[1,1,1],
            height=textHeight,
            wrapWidth=wrap,
            alignText="left"
        )
        
        prepForConditionRound2_pg1Repeating= visual.TextStim(
            win,
            text='Before we begin ROUND 2 of the gambling task, you will be asked to read a brief reminder of the instructions that were given in round 1.\n\n\n\nPress ‘enter’ to continue.',
            pos = (0,0),
            color=[1,1,1],
            height=textHeight,
            wrapWidth=wrap,
            alignText="left"
        )
        
        prepForConditionRound2_pg2forAllSubs = visual.TextStim(
            win,
            text='Please let the experimenter know when you are done reading the instructions.\n\n\n\nPress ‘enter’ to continue.',
            pos = (0,0),
            color=[1,1,1],
            height=textHeight,
            wrapWidth=wrap,
            alignText="left"
        )
        
        
        # CONTROL INSTRUCTIONS (FIRST TIME AROUND)
        controlInst1 = visual.TextStim(
            win,
            text='In this round of the task, please make your choices however you normally would, considering all factors that you naturally would notice or think about. \n\nPrevious research has found that people use all kinds of information to make choices in risky contexts. \n\n\nPress ‘enter’ to continue.',
            pos = (0,0),
            color=[1,1,1],
            height=textHeight,
            wrapWidth=wrap,
            alignText="left"
        )
        
        controlInst2 = visual.TextStim(
            win,
            text='Knowing how the task works, don’t try to control your thoughts any more than you would normally, and take as much of a natural approach to your decisions as you can, whatever that might mean for you. \n\nMake your choices in a way that makes sense to you, given any goals, rules of thumb, or factors you think or feel are important. \n\n\nPress ‘enter’ to continue.',
            pos = (0,0),
            color=[1,1,1],
            height=textHeight,
            wrapWidth=wrap,
            alignText="left"
        )
        
        controlInst3 = visual.TextStim(
            win,
            text='For this round, focus on the task itself, and the events, options, and actions that you would naturally consider, and how you feel about them. \n\nIf you select the gamble, you have an equal chance of receiving either amount and if you select the safe option, that will be the outcome for that trial.\n\nYou will complete many trials in this round.\n\n\nPress ‘enter’ to continue.',
            pos = (0,0),
            color=[1,1,1],
            height=textHeight,
            wrapWidth=wrap,
            alignText="left"
        )
        
        controlInst4 = visual.TextStim(
            win,
            text='On each trial, let your thoughts, feelings, impulses, and goals guide your decision-making as naturally as possible, without trying to change, eliminate, or emphasize them beyond how you might otherwise naturally. \n\nRemember that you will be paid the outcome of one randomly selected trial, and simply try to make the best choices you can. \n\nFor this round, approach the task and evaluate your choice options as you would naturally, without trying to control or change your approach. \n\n\nPress ‘enter’ to continue.',
            pos = (0,0),
            color=[1,1,1],
            height=textHeight,
            wrapWidth=wrap,
            alignText="left"
        )
        
        
        controlReminder1  = visual.TextStim(
            win,
            text='As a reminder, in this round of the task, please make your choices however you normally would.\n\nOn each trial, let your thoughts, feelings, impulses, and goals guide your decision-making as naturally as possible, without trying to change, eliminate, or emphasize them beyond how you might otherwise naturally. \n\n\nPress ‘enter’ to continue.',
            pos = (0,0),
            color=[1,1,1],
            height=textHeight,
            wrapWidth=wrap,
            alignText="left"
        )
        
        controlReminder2 = visual.TextStim(
            win,
            text='Simply try to make the best choices you can.\n\nFor this round, approach the task and evaluate your choice options as you would naturally, without trying to control or change your approach.\n\n\nPress ‘enter’ to continue.',
            pos = (0,0),
            color=[1,1,1],
            height=textHeight,
            wrapWidth=wrap,
            alignText="left"
        )
        
        
        # STRATEGY INSTRUCTIONS (FIRST TIME AROUND)
        
        stratInst1 = visual.TextStim(
            win,
            text='In this round of the task, please make your choices in isolation from any context, considering each choice solely on its own merits. \n\nIn our previous studies involving this gambling task, we have found that participants’ choices to accept the gamble were influenced not only by the options on the current trial but also depended on what happened earlier in the task.\n\n\nPress ‘enter’ to continue.',
            pos = (0,0),
            color=[1,1,1],
            height=textHeight,
            wrapWidth=wrap,
            alignText="left"
        )
        
        stratInst2 = visual.TextStim(
            win,
            text='Each trial in this task is unrelated to previous trials. \n\nThe values and outcomes of previous trials do not influence the outcome of the current trial. \n\nAllowing previous values and outcomes to influence your current choice may lead to a lower payoff, and thus not maximize the money you receive.\n\n\nPress ‘enter’ to continue.',
            pos = (0,0),
            color=[1,1,1],
            height=textHeight,
            wrapWidth=wrap,
            alignText="left"
        )
        
        stratInst3 = visual.TextStim(
            win,
            text='For each decision in this round, focus on the monetary values on the screen, the probability of receiving each of those options, and how you feel about them. \n\nForget about the previous values, choices, and outcomes and simply focus on the current trial. \n\nIf you select the gamble, you have an equal chance of receiving either amount and if you select the safe option, that will be the outcome for that trial. \n\nThis is true regardless of what has happened earlier in the task. \n\n\nPress ‘enter’ to continue.',
            pos = (0,0),
            color=[1,1,1],
            height=textHeight,
            wrapWidth=wrap,
            alignText="left"
        )
        
        stratInst4 = visual.TextStim(
            win,
            text='Remember that you will be paid the outcome of one randomly selected trial.\n\nOn each trial, think about how you would feel if the outcome on this trial was randomly selected as your cash payment.\n\nFor this round, approach the task and evaluate your choice options with a focus on only that choice, in isolation from any context.\n\n\nPress ‘enter’ to continue.',
            pos = (0,0),
            color=[1,1,1],
            height=textHeight,
            wrapWidth=wrap,
            alignText="left"
        )
        
        strategyReminder1  = visual.TextStim(
            win,
            text='As a reminder, in this round of the task, please make your choices in isolation from any context, considering each choice solely on its own merits.\n\nOn each trial, focus on the monetary values on the screen, the probability of receiving each of those options, and how you feel about them.\n\n\nPress ‘enter’ to continue.',
            pos = (0,0),
            color=[1,1,1],
            height=textHeight,
            wrapWidth=wrap,
            alignText="left"
        )
        
        strategyReminder2 = visual.TextStim(
            win,
            text='Forget about the previous values, choices, and outcomes and simply focus on the current trial.\n\nThink about how you would feel if the outcome on this trial was randomly selected as your cash payment.\n\nFor this round, approach the task and evaluate your choice options with a focus on only that choice, in isolation from any context.\n\n\nPress ‘enter’ to continue.',
            pos = (0,0),
            color=[1,1,1],
            height=textHeight,
            wrapWidth=wrap,
            alignText="left"
        )
        
        # screen count for instructions
        instructCount = visual.TextStim(
            win,
            pos =[scrnsize[1]*.95,-360],
            color=[1,1,1],
            height=textHeight/2,
            wrapWidth=wrap,
            alignText="left"
        ) 
        
        
        summarizeInst = visual.TextStim(
            win,
            text='Please let the experimenter know that you are done reading the instructions. \n\nIf you wish to read the instructions again, press "R".',
            pos = (0,0),
            color=[1,1,1],
            height=textHeight,
            wrapWidth=wrap,
            alignText="left"
        )
        
        startTaskRound1 = visual.TextStim(
            win, 
            text='The experimenter will now leave the room.\n\nOnce the experimenter leaves the room, you may begin ROUND 1 of the gambling task. \n\nPress "V" or "N" to begin the task.', 
            pos = (0,0),
            color=[1,1,1],
            height = textHeight,
            wrapWidth =wrap,
            alignText="left"
        )
        
        
        startTaskRound2 = visual.TextStim(
            win, 
            text='The experimenter will now leave the room.\n\nOnce the experimenter leaves the room, you may begin ROUND 2 of the gambling task. \n\nPress "V" or "N" to begin the task.', 
            pos = (0,0),
            color=[1,1,1],
            height = textHeight,
            wrapWidth = wrap,
            alignText="left"
        )
        
        postTask1 = visual.TextStim(
            win, 
            text='ROUND 1 of the task is complete! \n\nRandomly selecting outcome...', 
            pos = (0,0),
            color=[1,1,1],
            height = textHeight,
            wrapWidth = wrap,
            alignText="left"
        )
        
        postTask2 = visual.TextStim(
            win, 
            text='ROUND 2 of the task is complete! \n\nRandomly selecting outcome...', 
            pos = (0,0),
            color=[1,1,1],
            height = textHeight,
            wrapWidth = wrap,
            alignText="left"
        )
        
        ocSelect = visual.TextStim(
            win,  
            pos = (0,0),
            color=[1,1,1],
            height =textHeight,
            wrapWidth=wrap,
            alignText="left"
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
            height =textHeight
        )
        
        
        nTxt = visual.TextStim(
            win=win,
            text='N - Right',
            color = [1,1,1],
            font='Helvetica',
            pos=[centerR[0],100-radius*1.5],
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
            height =moneyTextHeight
        )
        
        lossTxt = visual.TextStim(
            win=win,
            color = [-1,-1,-1],
            font='Helvetica',
            height =moneyTextHeight
        )
        
        altTxt = visual.TextStim(
            win=win,
            color = [-1,-1,-1],
            font='Helvetica',
            height =moneyTextHeight
        )
        
        orTxt = visual.TextStim(
            win=win,
            text="OR",
            pos=center,
            color = [1,1,1],
            font='Helvetica',
            height =textHeight
        )
        
        #ISI STIMULI (iti will use same stimuli):
        isiStim = visual.Circle(
            win=win,
            units="pix",
            pos=center,
            radius=1,
            fillColor=[1, 1, 1],
            lineColor=[1, 1, 1],
            edges =128 #make the circle smoother
        )
        
        itiStim = isiStim
        
        # OUTCOME stimuli
        noRespTxt = visual.TextStim(
            win=win,
            text='You did not respond in time.',
            color = [1,1,1],
            font='Helvetica',
            pos=center,
            height =textHeight,
            wrapWidth = wrap
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
        
        # PROGRESS BARS
        # this is the dimension where the progres bar starts
        progBarStart = [scrnsize[1]*-.45,scrnsize[1]*-.375]
        progBarEnd = [progBarStart[0]+5,progBarStart[1]]
        
        progBar = visual.Line(
            win, 
            start=progBarStart, 
            end=progBarEnd, 
            units='pix', 
            lineWidth=textHeight*.35, 
            lineColor='white'
        )
        
        progBarOutline = visual.Rect(
            win, 
            width=((progBarStart[0]*-1)+10)*2, 
            height=textHeight/2, 
            units='pix', 
            pos=[center[0],progBarStart[1]], 
            lineColor = "white", 
            fillColor=None
        )
        
        
        # Text for for progress bar (text will dynamically update below)
        progressTxt = visual.TextStim(
            win,
            color="white",
            pos =[progBarStart[0]+25,-360],
            height = textHeight/2
        ) 
        
        
        #POST TASK QUESTIONS STIMULI
        promptPostQ= visual.TextStim( # In round #, you were asked to...(text is dynamically updated based on condition below)
            win, 
            pos = (0,scrnsize[1]*.25),
            color=[1,1,1],
            height = textHeight,
            wrapWidth = wrap,
            alignText="left",
        )
        
        sliderLockPostQ= visual.TextStim( # rating recorded
            win, 
            pos = (0,scrnsize[1]*-.35),
            color=[.5,0,.5],
            height = textHeight*.8,
            wrapWidth = wrap,
            alignText="center",
            text="Rating recorded!"
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
        
        #nPract=3 # number of practice trials
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
            
        
        # define variable that is used to change the size of the progress bar
        changeInBar = int((progBarStart[0]/nPract)*-1)*2 # double it because it needs to go across the entire screen (not just half)
        
        
        pracStart = core.Clock() # starts clock for practice 
        #pracStart.reset() # resets the clock
            
        for p in range(nPract):
            
            t = p+1 # to make t (trial) = 1 since python starts at 0
        
            
            progBar.end += [changeInBar,00] # update end point of progress bar
            progressTxt.text = text= "Trial %d/%d " % (t,nPract)
            
            progressTxt.draw() # draws the message to the window, but only during the loop
            progBarOutline.draw()
            progBar.draw()
        
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
            progBar.draw()        
        
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
            progBar.draw()   
            
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
            progBar.draw()   
            ocTxt.draw()
            win.flip() # show it
            outcomeDispStart = pracStart.getTime()
            core.wait(outcomeTime)
        
            #ITI    
            itiStart = pracStart.getTime()
            while pracStart.getTime() < t*(stimTime + choiceTime + isi + outcomeTime) + sum(itiPract[0:t]):
                
                progressTxt.draw() # draws the message to the window, but only during the loop
                progBarOutline.draw()
                progBar.draw()   
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
    
    
    #practiceData = pd.DataFrame(practiceData) #convert data into pandas dataframe
    
    
    # save practice file
    #datetime = time.strftime("%Y%m%d-%H%M%S"); # save date and time
    #filename = "rcsRDMpractice_" + "sub" + subID + "_" + datetime + ".csv"; # make filename
    #practiceData.to_csv(filename)
    
    
    #----------Start the task---------#
    #try:
    
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
                "roundRDM",
                "roundColor"
            ]
        )
        
        postQdata=[]
        postQdata.append(
            [
                "subID",
                "difficulty",
                "howOften"
            ]
        )
    
        trialOutcome = []
        trialOutcome.append(
            [
                "subID",
                "trial",
                "outcome"
            
            ]
        )
        
        # define the increment for increasing progress bar based on number of trials 
        changeInBar = int((progBarStart[0]/nT)*-1)*2 # double it because it needs to go across the entire screen (not just half)
        
        
        for r in range(RDMrounds):
            
            #reset the progress bar end point at the start of each round
            progBar.end = progBarEnd 
             
            # which progress bar and outline will we show?
            if colorOrder[r] == 0:
                progBar.color =[0,.6,0]
                borderBox.color =[0,.6,0]
            elif colorOrder[r] ==1:
                progBar.color = [.5,0,.5]
                borderBox.color=[.5,0,.5] 
                            
            
            # generate the choiceset on each round and save the choice set
            rcsCS = rcsRDMChoiceSet.rcsRDMChoiceSet()
            
            # save the choice set for each round of the task
            rcsCSdf = pd.DataFrame(rcsCS)
    
            # save file
            datetime = time.strftime("%Y%m%d-%H%M%S"); # save date and time
            filenameRDMchoiceset = dataDirectoryPath + "rcsRDM_choiceSet_round" + str(r) + "_sub" + subID + "_" + datetime + ".csv"; # make filename
            rcsCSdf.to_csv(filenameRDMchoiceset)
                
           
            # store some of the choice set features in new variables
            riskyGain = rcsCS['riskyGain']
            riskyLoss = rcsCS['riskyLoss']
            safe = rcsCS['alternative']
            evLevel = rcsCS['evLevel']
            evInd = rcsCS['evInd']
            runSize = rcsCS['runSize']
        
        
        
            #ITIs change as a function of choiceset
            iti = rcsCS['iti']
        
        
    

            # show our round separation theatric stuff
            if r ==0: 
                explainRounds.draw()
                win.flip()
                event.waitKeys(keyList = ['return'], timeStamped=False)
                
                readyForRound1.draw()
                win.flip()
                event.waitKeys(keyList = ['return'], timeStamped=False)
                
                startingRound1.draw()
                win.flip()
                core.wait(1)
            
            elif r==1:
                round2Prep.draw()
                win.flip()
                event.waitKeys(keyList = ['return'], timeStamped=False)
                
                readyForRound2.draw()
                win.flip()
                event.waitKeys(keyList = ['return'], timeStamped=False)
                
                startingRound2.draw()
                win.flip()
                core.wait(1)
            
                
    
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
            
            # set up border color
            borderBox.draw() # draw the large color box
            blackBox.draw() # draw smaller black box on top of our color rect to create border effect
            
    
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
            
            #Offer participants the option to re-read the instructions where they can pres 'R' after page 4
            keepLoopGoing = True
            while keepLoopGoing:  
            
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
                    instructCount.text=text="screen 1/4"
                    instructCount.draw()
        
                    win.flip()
                    event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press 
                    
                    #show page 2
                    borderBox.draw() # draw the large color box
                    blackBox.draw() # draw smaller black box on top of our color rect to create border effect
                    
                    instructPG2.draw()
                    instructCount.text=text="screen 2/4"
                    instructCount.draw()
        
                    win.flip()
                    event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press 
                    
                    #show page 3
                    borderBox.draw() # draw the large color box
                    blackBox.draw() # draw smaller black box on top of our color rect to create border effect
                    
                    instructPG3.draw()
                    instructCount.text=text="screen 3/4"
                    instructCount.draw()
        
                    win.flip()
                    event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press 
                    
                    #show page 4
                    borderBox.draw() # draw the large color box
                    blackBox.draw() # draw smaller black box on top of our color rect to create border effect
                    
                    instructPG4.draw()
                    instructCount.text=text="screen 4/4"
                    instructCount.draw()
        
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
                    instructCount.text=text="screen 1/2"
                    instructCount.draw()
                    
                    win.flip()
                    event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press 
                     
                    #show page 2
                    borderBox.draw() # draw the large color box
                    blackBox.draw() # draw smaller black box on top of our color rect to create border effect
                     
                    instructPG2.draw()
                    instructCount.text=text="screen 2/2"
                    instructCount.draw()
        
                    win.flip()
                    event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press 
         
        
        
                # Now the rest is mostly the same for all participants/conditions/switching show the summarize prompt
                borderBox.draw() # draw the large color box
                blackBox.draw() # draw smaller black box on top of our color rect to create border effect
                
                summarizeInst.draw()
                win.flip()
                
                
                keys = event.waitKeys(keyList = ['return','r'], timeStamped = False) # waiting for key press
                #print(keys)
                
                #print(keys[0] == 'return')
                
                if keys[0] == 'return':
                    keepLoopGoing=False # end loop, start task
                else:
                    keepLoopGoing=True
            
            
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
    
                            
                progBar.end += [changeInBar,00]
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
                progBar.draw()
                
            
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
                progBar.draw()
                
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
                progBar.draw()
                
                isiStim.draw()
                win.flip() # show it
                isiStart = rdmStart.getTime()
                core.wait(isi)
            
                #DO THE OUTCOME
                borderBox.draw() # draw the large color box
                blackBox.draw() # draw smaller black box on top of our color rect to create border effect
                progressTxt.draw() # draws the message to the window, but only during the loop
                progBarOutline.draw()
                progBar.draw()
                
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
                    progBar.draw()
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
                        r+1,
                        colorOrder[r]
                    ]
                )
                
                    
            
            
            datatopickoutcomes = pd.DataFrame(data[1:len(data)], columns = data[0]) # convert to dataframe
            datatopickoutcomes = datatopickoutcomes.loc[datatopickoutcomes['roundRDM'] == (r+1)]; # just want the one round
            allOutcomes = datatopickoutcomes['outcome'] # save just the outcomes
            
            # select an outcome to pay participant
            realOutcomes = datatopickoutcomes[allOutcomes != 'NaN'] 
      
            
            trialSelected = np.random.choice(realOutcomes['trial']) # randomly select a trial
            ocSelected = realOutcomes['outcome'][realOutcomes['trial']==trialSelected] # pull out outcome based on randomly selected trial
            ocSelected = ocSelected.iat[0] # this removes the extra information like float, name, etc.
            
            #data.append([ocChosen])
            trialOutcome.append(
                [
                    subID,
                    trialSelected,
                    ocSelected
                ]
            )
            
            borderBox.draw() # draw the large color box
            blackBox.draw() # draw smaller black box on top of our color rect to create border effect
            
            if r ==0:
                postTask1.draw() #"randomly selecting outcome..."
            elif r==1:
                postTask2.draw()
            win.flip()
            core.wait(2)
        
            
            if r==0:
                ocSelect.text= text='ROUND 1\n\nRandomly selected trial: %d \n\nOutcome on trial %d: $%.2f. \n\nThis will be one of the outcomes considered for payment at the end of the study. \n\nYou will now be asked two questions about your experience in the task. \n\nPress ‘enter’ to continue.' % (trialSelected,trialSelected, ocSelected)
            elif r==1:
                ocSelect.text= text='ROUND 2\n\nRandomly selected trial: %d \n\nOutcome on trial %d: $%.2f. \n\nThis will be one of the outcomes considered for payment at the end of the study. \n\nYou will now be asked two questions about your experience in the task. \n\nPress ‘enter’ to continue.' % (trialSelected, trialSelected, ocSelected)
            
            borderBox.draw() # draw the large color box
            blackBox.draw() # draw smaller black box on top of our color rect to create border effect
            ocSelect.draw() #"You will receive ..."
            win.flip()
            event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press 
            

            # 2 post-task questions
            taskRound = r+1 # change the round  to 1 or 2 (versus python's 0 or 1)
            
            
            # set color of marker and repsonse recorded text
            if colorOrder[r] ==0:
                sliderColor=[0,.6,0] # green
                sliderLockPostQ.color=[0,.6,0] 
            elif colorOrder[r] ==1:
                sliderColor=[.5,0,.5] # purple
                sliderLockPostQ.color=[.5,0,.5]
            
            
            # Question 1: DIFFICULTY
            if strategy ==0: # control condition
                promptPostQ.text=text="\n\nQuestion 1/2 \n\nFor ROUND %d, you were asked to make your choices as you would naturally, without trying to control or change your approach. \n\n\nHover the mouse over the scale to move the point on the slider to rate how DIFFICULT this was and click when you are done:" % taskRound
     
            elif strategy ==1:
                promptPostQ.text=text="\n\nQuestion 1/2 \n\nFor ROUND %d, you were asked to make your choices in isolation from any context, considering each choice solely on its own merits. \n\n\nHover the mouse over the scale to move the point on the slider to rate how DIFFICULT this was and click when you are done:" % taskRound
            

        
            # For some reason, slider.labels is not showing up dynamically, so we reset it here to make labels fit the question
            slider = visual.Slider(
                win, 
                size=(scrnsize[0]*.8, 50), 
                pos=(0, scrnsize[1]*-.25),
                labels = ['Very \neasy', 'Very \ndifficult'],
                ticks = [1,100],
                granularity=0, 
                style=['rating'],
                color=sliderColor, 
                font='Helvetica',
                labelHeight=30,
            )


        
            
            slider_width = slider.size[0]
            slider_height = slider.size[1]
            slider_orientation = 0
            slider_ticks = [0,100]

    
    
            slider_shape = visual.Rect(
                win=win, 
                name='slider_shape',
                width=(slider_width, slider_height)[0], 
                height=(slider_width, slider_height)[1],
                ori=0, 
                pos=slider.pos,
                lineWidth=1, 
                lineColor='black', 
                lineColorSpace='rgb',
                fillColor='black', 
                fillColorSpace='rgb',
                opacity=1, 
                depth=-2.0, 
                interpolate=True
            )
    
             
            slider.markerPos = 50
            slider.marker.color = sliderColor
            
            slider_shape.draw()
            borderBox.draw()
            blackBox.draw()
            promptPostQ.draw()
            slider.draw()
    
            win.flip()

            mouse = event.Mouse(visible = True, win = win) 
            mouseRec=mouse.getPos()
    
    
    
            continueRout=True
            while continueRout:
                if slider.markerPos and mouse.isPressedIn(slider_shape):
                    continueRout = False
                elif slider_shape.contains(mouse) and mouse.getPos()[slider_orientation] != mouseRec[slider_orientation]:
                    mouseRec=mouse.getPos()
                    slider.markerPos=mouseRec[slider_orientation]/slider_width*(slider_ticks[-1]-slider_ticks[0])+(slider_ticks[0]+slider_ticks[-1])/2
                    slider_shape.draw()
                    borderBox.draw()
                    blackBox.draw()
                    promptPostQ.draw()
                    slider.draw()
                    win.flip()
    

                    
            difficultyRating = slider.markerPos# store rating
            slider_shape.draw()
            borderBox.draw() # draw the large color box
            blackBox.draw() # draw smaller black box on top of our color rect to create border effect
            sliderLockPostQ.draw() #"rating recorded"
            promptPostQ.draw()
            slider.draw()
            win.flip()
            core.wait(2)
                            
            
            # Question 2: HOW OFTEN 
            if strategy ==0: # control condition
                promptPostQ.text=text="\n\nQuestion 2/2 \n\nFor ROUND %d, you were asked to make your choices as you would naturally, without trying to control or change your approach. \n\n\nHover the mouse over the scale to move the point on the slider to rate HOW OFTEN you were able to do that and click the mouse when you are done:" % taskRound
     
            elif strategy ==1:
                promptPostQ.text=text="\n\nQuestion 2/2 \n\nFor ROUND %d, you were asked to make your choices in isolation from any context, considering each choice solely on its own merits. \n\n\nHover the mouse over the scale to move the point on the slider to rate HOW OFTEN you were able to do that and click the mouse when you are done:" % taskRound
                
                
                    
            # For some reason, slider.labels is not showing up dynamically, so we reset it here to make labels fit the question
            slider = visual.Slider(
                win, 
                size=(scrnsize[0]*.8, 50), 
                pos=(0, scrnsize[1]*-.25),
                labels = ['Never', 'Always'],
                ticks = [1,100],
                granularity=0, 
                style=['rating'],
                color=sliderColor, 
                font='Helvetica',
                labelHeight=30,
            )
    

             
            slider.markerPos = 50
            slider.marker.color = sliderColor
            
            slider_shape.draw()
            borderBox.draw()
            blackBox.draw()
            promptPostQ.draw()
            slider.draw()
    
            win.flip()

            mouse = event.Mouse(visible = True, win = win) 
            mouseRec=mouse.getPos()
    
    
    
            continueRout=True
            while continueRout:
                
                if slider.markerPos and mouse.isPressedIn(slider_shape):
                    continueRout = False
                elif slider_shape.contains(mouse) and mouse.getPos()[slider_orientation] != mouseRec[slider_orientation]:
                    mouseRec=mouse.getPos()
                    slider.markerPos=mouseRec[slider_orientation]/slider_width*(slider_ticks[-1]-slider_ticks[0])+(slider_ticks[0]+slider_ticks[-1])/2
                    slider_shape.draw()
                    borderBox.draw()
                    blackBox.draw()
                    promptPostQ.draw()
                    slider.draw()
                    win.flip()
    

                    
            howOftenRating = slider.markerPos # store rating
            slider_shape.draw()
            borderBox.draw() # draw the large color box
            blackBox.draw() # draw smaller black box on top of our color rect to create border effect
            sliderLockPostQ.draw() #"rating recorded"
            promptPostQ.draw()
            slider.draw()
            win.flip()
            core.wait(2)
    

              
            postQdata.append(
                [
                    subID,
                    difficultyRating,
                    howOftenRating
                ]
            )
    
            #press white button for experimenter to come back in the room - it only happens in this spot following round 1
            if r == 0:
                callExperimenter.draw()
                win.flip()
                event.waitKeys(keyList = ['space'], timeStamped = False) # waiting for key press 
    
            
        #RANDOMLY SELECT OUTCOME FROM BOTH ROUNDS FOR PAYMENT
        trialOutcomeDF = pd.DataFrame(trialOutcome)
        finalOutcomesToSelect = [trialOutcomeDF[2][1], trialOutcomeDF[2][2]]
        outcomeForPay = np.random.choice(finalOutcomesToSelect);
        
        ocSelect.text = text = "The computer will now randomly select 1 of the 2 randomly selected outcomes from the gambling tasks. \n\nOutcome from ROUND 1: $%.2f \n\nOutcome from ROUND 2: $%.2f \n\n\nPress 'enter' to view your payment." % (finalOutcomesToSelect[0],finalOutcomesToSelect[1])
        
        ocSelect.draw()
        win.flip()
        event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press 
    
    
        ocSelect.text = text = "Randomly selected outcome: $%.2f. \n\n\nPress the white button to call the experimenter." % outcomeForPay
        ocSelect.draw()
        win.flip()
        event.waitKeys(keyList = ['space'], timeStamped = False) # waiting for key press 
        
        trialOutcome.append([outcomeForPay]) # save outcome payment.
        
    finally: # this should save the data even if something in "try" fails
        win.close()
        
        
               
        # if data exists, reformat to pandas dataframe if it wasn't above, and save it
        # save practice file
  
        datetime = time.strftime("%Y%m%d-%H%M%S"); # save date and time
        
        if 'data' in locals(): 
            if not isinstance(data, pd.DataFrame):
                data = pd.DataFrame(data)
                data.columns = ["subID","riskyGain", "riskyLoss","safe", "RT", "loc", "response", "choice","outcome","iti","evLevel","evInd","runSize","strategy","stimDispStart","choiceTimeStart","isiStart","outcomeDispStart","itiStart","trial","roundRDM","roundColor"]
                data = data.iloc[1: , :] # drop the first row which are the variable names
            filenameRDM = dataDirectoryPath + "rcsRDM_" + "sub" + subID + "_" + datetime + ".csv"; # make filename
            data.to_csv(filenameRDM)
        
            
        if 'postQdata' in locals(): 
            if not isinstance(postQdata, pd.DataFrame):
                postQdata = pd.DataFrame(postQdata) #convert data into pandas dataframe
                postQdata.columns=["subID","difficulty","howOften"] # add column names
                postQdata = postQdata.iloc[1: , :] # drop the first row which are the variable postQdata.iloc[1: , :] # drop the first row which are the variable names
            filenamePostQ = dataDirectoryPath + "rcsPostQ_" + "sub" + subID + "_" + datetime + ".csv"; # make filename
            postQdata.to_csv(filenamePostQ)
        
        if 'trialOutcome' in locals(): 
            if not isinstance(trialOutcome, pd.DataFrame):
                trialOutcome = pd.DataFrame(trialOutcome) #convert data into pandas dataframe
                trialOutcome.columns=["subID","trial","outcome"] # add column names
                trialOutcome = trialOutcome.iloc[1: , :] # drop the first row which are the variable trialOutcome.iloc[1: , :] # drop the first row which are the variable names
            filenameTrialOutcome = dataDirectoryPath + "rcsTrialOutcome_" + "sub" + subID + "_" + datetime + ".csv"; # make filename
            trialOutcome.to_csv(filenameTrialOutcome)
                
        if 'practiceData' in locals(): 
            if not isinstance(practiceData, pd.DataFrame):
                practiceData = pd.DataFrame(practiceData) #convert data into pandas dataframe
                practiceData.columns=["riskyGain", "riskyLoss", "safe", "RT", "loc", "response", "choice","outcome","iti","stimDispStart","choiceTimeStart","isiStart","outcomeDispStart","itiStart","trial"] # add column names
                practiceData = practiceData.iloc[1: , :] # drop the first row which are the variable practiceData.iloc[1: , :] # drop the first row which are the variable names
            filenamePrac = dataDirectoryPath + "rcsRDMpractice_" + "sub" + subID + "_" + datetime + ".csv"; # make filename
            practiceData.to_csv(filenamePrac)
         
    
        
        


       


    

    
    
    
    
    
