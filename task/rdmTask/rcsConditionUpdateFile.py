#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 04:51:26 2022

@author: shlab
"""


import pandas as pd
import numpy as np
import random, copy

# At this point, we have 106 participants (excluding 6) and the goal is to get another 20-50 more (depending on chits and subject pool availability)
# we will even out the groups with the next 8 participants
# then we will have evennumber of people in each condition every 8 participants (except for the last 8, we even the groups out every 4 people - this is likely to be changed if morepeople are excluded)
# the goal is to pass 30 people per group and will not get more than 39 people per group (after exclusion is applied) 



# import the conditions file
# this condition file has 125 rows where the excluded participant condition codes have been added to the end
# we originally planned for 120 participants but will now be going for 159 (more or less depending on funds, etc)
#condFile = pd.read_csv('/Users/shlab/Documents/GitHub/rcs/task/rdmTask/rcsConditions.csv')
#condFile = pd.read_csv('/Users/shlab/Documents/GitHub/rcs/task/rdmTask/rcsConditionsUpdated_Winter_wks1-4.csv') # load most recent conditions file to update it
condFile = pd.read_csv('/Users/shlab/Documents/GitHub/rcs/task/rdmTask/rcsConditionsUpdated_Winter.csv')


nSubComplete = 114
subIDExclude = [12,15,22,28,67,105] 
subIDExcludeIndex = [11,14,21,27,66,104] # python starts at zero so the index for the excluded participants is one less than their ID



# calculate number of conditions we have completed so far (excluding the exclusions)

completeCondFileFull = condFile[0:nSubComplete] #includes excluded participants

#completeCondFile = completeCondFileFull.drop(labels = subIDExclude, axis = 0) # drop the rows from excluded participants
completeCondFile = completeCondFileFull.drop(labels = subIDExcludeIndex, axis = 0) # drop the rows from excluded participants


# number of participants in each condition as of 1/27/23 from participant data we are including:

cond1count = sum(completeCondFile.condCode==1) # 27
cond2count = sum(completeCondFile.condCode==2) # 27
cond3count = sum(completeCondFile.condCode==3) # 27
cond4count = sum(completeCondFile.condCode==4) # 27

# 1/27/24 let's even the groups out every 4 participants because data collection is slow and we could end shortly.
    
# We need 12 more people to get to n=120 (30 per group), so let's start with the next 12 participants and then afterward, we will even groups out every 4 participants
    



orderList =  np.repeat([1,2,3,4],3) # repeat each condition the desired number of times
random.shuffle(orderList); #shuffle the order


# do the same for the color assignment
colorCount1 = sum((completeCondFile.cond1color==0) & (completeCondFile.cond2color ==1)) #50 green then purple
colorCount2 = sum((completeCondFile.cond1color==1) & (completeCondFile.cond2color ==0)) #50 purple then green



# color order is even right now, so for the next 12 people, split up into 6
colorOrderList = np.repeat([1,2], [6])
random.shuffle(colorOrderList)



subIDlist = np.array([i for i in range(115,127)]); # subIds 115 to 126


# make columns for condition for round1 1 and round 2 of gambling task
# where 0 = control condition
# where 1 = strategy condition

# copying the orderlist for cond1 and cond2 variables
cond1 = copy.copy(orderList); 
cond2 = copy.copy(orderList);


# some conditional statements
# control condition first
cond1[[i for i, j in enumerate(cond1) if j == 1]]= 0
cond1[[i for i, j in enumerate(cond1) if j == 2]]= 0

# strategy condition first
cond1[[i for i, j in enumerate(cond1) if j == 3]]= 1
cond1[[i for i, j in enumerate(cond1) if j == 4]]= 1


# control condition second
cond2[[i for i, j in enumerate(cond2) if j == 1]]= 0
cond2[[i for i, j in enumerate(cond2) if j == 3]]= 0

# strategy condition second
cond2[[i for i, j in enumerate(cond2) if j == 2]]= 1
cond2[[i for i, j in enumerate(cond2) if j == 4]]= 1


# make columns for color order for round1 1 and round 2 of gambling task
# where 0 = green
# where 1 = purple

cond1color = copy.copy(colorOrderList)
cond2color = copy.copy(colorOrderList)

cond1color[[i for i, j in enumerate(cond1color) if j == 1]]= 0 # green for round 1
cond1color[[i for i, j in enumerate(cond1color) if j == 2]]= 1 # purple for round 1


cond2color[[i for i, j in enumerate(cond2color) if j == 2]]= 0 # green for round 2 (don't need to change 1 because that already means purple is second)



tmpdata = {
  "condCode": orderList,
  "subID": subIDlist,
  "cond1": cond1,
  "cond2": cond2,
  "cond1color": cond1color,
  "cond2color": cond2color
}

DF1 = pd.DataFrame(tmpdata)



# then for the following for or set of 20 people, then it should be 5 participants per condition (this may change depending on exclusions).
# and half do green then purple and the other half to purple then green

subIDlistDF2 = np.array([i for i in range(127,155)]); # subIds 127 to 154 (1/27/23: with no additional exclusions 154 total subs = 148 included = 37 subs per condition)

orderList2 =  np.repeat([1,2,3,4], 1) # repeat each condition the desired number of times (subs: 127-130)
random.shuffle(orderList2); #shuffle the order

orderList3 =  np.repeat([1,2,3,4], 1) # repeat each condition the desired number of times (subs: 131-134)
random.shuffle(orderList3); #shuffle the order

orderList4 =  np.repeat([1,2,3,4], 1) # repeat each condition the desired number of times (subs: 135-138)
random.shuffle(orderList4); #shuffle the order

orderList5 =  np.repeat([1,2,3,4], 1) # repeat each condition the desired number of times (subs: 139-142)
random.shuffle(orderList5); #shuffle the order

orderList6 =  np.repeat([1,2,3,4], 1) # repeat each condition the desired number of times (subs: 143-146)
random.shuffle(orderList6); #shuffle the order

orderList7 =  np.repeat([1,2,3,4], 1) # repeat each condition the desired number of times (subs: 147-150)
random.shuffle(orderList7); #shuffle the order

orderList8 =  np.repeat([1,2,3,4], 1) # repeat each condition the desired number of times (subs: 151-154) #not that we are reaching this number and the final values will probably change based on exclusion
random.shuffle(orderList8); #shuffle the order



colorOrder2 = np.repeat([1,2],2)
random.shuffle(colorOrder2); #shuffle the order

colorOrder3 = np.repeat([1,2],2)
random.shuffle(colorOrder3); #shuffle the order

colorOrder4 = np.repeat([1,2],2)
random.shuffle(colorOrder4); #shuffle the order

colorOrder5 = np.repeat([1,2],2)
random.shuffle(colorOrder5); #shuffle the order

colorOrder6 = np.repeat([1,2],2)
random.shuffle(colorOrder6); #shuffle the order

colorOrder7 = np.repeat([1,2],2)
random.shuffle(colorOrder7); #shuffle the order

colorOrder8 = np.repeat([1,2],2)
random.shuffle(colorOrder8); #shuffle the order







# make columns for condition for round1 1 and round 2 of gambling task
# where 0 = control condition
# where 1 = strategy condition

# copying the orderlist for cond1 and cond2 variables and combine the np arrays for weeks 2-4 into one
orderList_all = np.concatenate((orderList2,orderList3,orderList4, orderList5, orderList6, orderList7, orderList8))
cond1 = copy.copy(orderList_all)
cond2 = copy.copy(orderList_all)


# some conditional statements
# control condition first
cond1[[i for i, j in enumerate(cond1) if j == 1]]= 0
cond1[[i for i, j in enumerate(cond1) if j == 2]]= 0

# strategy condition first
cond1[[i for i, j in enumerate(cond1) if j == 3]]= 1
cond1[[i for i, j in enumerate(cond1) if j == 4]]= 1


# control condition second
cond2[[i for i, j in enumerate(cond2) if j == 1]]= 0
cond2[[i for i, j in enumerate(cond2) if j == 3]]= 0

# strategy condition second
cond2[[i for i, j in enumerate(cond2) if j == 2]]= 1
cond2[[i for i, j in enumerate(cond2) if j == 4]]= 1


# make columns for color order for round1 1 and round 2 of gambling task
# where 0 = green
# where 1 = purple


# copying the colorOrderlist for cond1 and cond2 variables and combine the np arrays for weeks 2-4 into one
colorOrderList_all = np.concatenate((colorOrder2, colorOrder3, colorOrder4, colorOrder5, colorOrder6, colorOrder7, colorOrder8))

cond1color = copy.copy(colorOrderList_all)
cond2color = copy.copy(colorOrderList_all)

cond1color[[i for i, j in enumerate(cond1color) if j == 1]]= 0 # green for round 1
cond1color[[i for i, j in enumerate(cond1color) if j == 2]]= 1 # purple for round 1


cond2color[[i for i, j in enumerate(cond2color) if j == 2]]= 0 # green for round 2 (don't need to change 1 because that already means purple is second)


tmpdata_theRest = {
  "condCode": orderList_all,
  "subID": subIDlistDF2,
  "cond1": cond1,
  "cond2": cond2,
  "cond1color": cond1color,
  "cond2color": cond2color
}

theRemainingConditions = pd.DataFrame(tmpdata_theRest)




# combine the three dataframes: conditions completed, week 1 ,and weeks 2-4

frames = [completeCondFileFull,DF1, theRemainingConditions] # a necessary step to combining the pd dataframes
bigDF = pd.concat(frames) # combine the frames we just created
bigDF = bigDF.reset_index(drop=True) # reset row numbers to be continuious from 0 to the end 




# change the subIDs to have leading zeroes to be consistent with the rest of the study, e.g. 001
bigDF['subID'] = bigDF['subID'].astype(str); # convert subIDs to strings

for i in range(len(bigDF.subID)):
    if i<9: # remember that python starts indexing at 0
        bigDF.subID[i] = "00" + bigDF.subID[i]
    elif i >=9 and i <99:
        bigDF.subID[i] = "0" + bigDF.subID[i]

#bigDF.subID = bigDF.subID.apply('="{}"'.format); # preserve leading zeroes
bigDF.subID = bigDF.subID.apply('{}'.format); # preserve leading zeroes

bigDF.to_csv("/Users/shlab/Documents/GitHub/rcs/task/rdmTask/rcsConditionsUpdated_Winter.csv", index=False) # save the csv file

