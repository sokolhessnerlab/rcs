#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 04:51:26 2022

@author: shlab
"""


import pandas as pd
import numpy as np
import random, copy

# At this point, we have 79 participants (excluding 5) and the goal is to get another 80 or so.
# The condition file as is, is not evenly weighted by when we get certain conditions (lots of 1 and 4 conditions but much less 2 and 3s)
# We are going to update the condition csv so that after each week (or roughtly 20 people), we have a similar number of people in each group

# as of 12/29/22 - if we collect 159 participants and do not exclude any more, we will have 38 participants in condition 1 and 4 and 39 in 2 and 3
# we can even this out toward the end depending on number of people excluded across the conditions and funds left over. 
# Ideally, we get even number of people in each condition.



# import the conditions file
# this condition file has 125 rows where the excluded participant condition codes have been added to the end
# we originally planned for 120 participants but will now be going for 159 (more or less depending on funds, etc)
condFile = pd.read_csv('/Users/shlab/Documents/GitHub/rcs/task/rdmTask/rcsConditions.csv')



nSubComplete = 79 
subIDExclude = [12,15,22,28,67] 



# calculate number of conditions we have completed so far (excluding the exclusions)

completeCondFileFull = condFile[0:nSubComplete] #includes excluded participants

completeCondFile = completeCondFileFull.drop(labels = subIDExclude, axis = 0) # drop the rows from excluded participants

# number of participants in each condition as of 12/29/22 from participant data we are including:

cond1count = sum(completeCondFile.condCode==1) # 21
cond2count = sum(completeCondFile.condCode==2) # 17
cond3count = sum(completeCondFile.condCode==3) # 14
cond4count = sum(completeCondFile.condCode==4) # 22



# then calcaute the number of ecah condition we need in the first week to even out number of poeple in the groups
# the goal of the first week is to collect data from 20 people = 94 people total so thats 23-24 people per group
# to get the conditions even after the first week, each group needs the following participants

    #cond 1 = 2 people
    #cond 2 = 7 people
    #cond 3 = 10 people
    #cond 4 = 1 people

orderList =  np.repeat([1,2,3,4], [2,7,10,1]) # repeat each condition the desired number of times
random.shuffle(orderList); #shuffle the order




# do the same for the color assignment
colorCount1 = sum((completeCondFile.cond1color==0) & (completeCondFile.cond2color ==1)) #33 green then purple
colorCount2 = sum((completeCondFile.cond1color==1) & (completeCondFile.cond2color ==0)) #41 purple then green

# to even out the color order for the next 20 people, 14 see green then purple and 6 see purple then green
colorOrderList = np.repeat([1,2], [14,6])
random.shuffle(colorOrderList)




subIDlist = np.array([i for i in range(80,100)]); # subIds 80 to 99


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

week1DF = pd.DataFrame(tmpdata)



# then for the following weeks or set of 20 people, then it should be 5 participants per condition (this may change depending on exclusions).
# and half do green then purple and the other half to purple then green

subIDlistWeeks2_3_4 = np.array([i for i in range(100,160)]); # subIds 100 to 159

orderListWeek2 =  np.repeat([1,2,3,4], 5) # repeat each condition the desired number of times
random.shuffle(orderListWeek2); #shuffle the order


orderListWeek3 =  np.repeat([1,2,3,4], 5) # repeat each condition the desired number of times
random.shuffle(orderListWeek3); #shuffle the order


orderListWeek4 =  np.repeat([1,2,3,4], 5) # repeat each condition the desired number of times
random.shuffle(orderListWeek4); #shuffle the order




colorOrderListWeek2 = np.repeat([1,2],10)
random.shuffle(colorOrderListWeek2); #shuffle the order

colorOrderListWeek3 = np.repeat([1,2],10)
random.shuffle(colorOrderListWeek3); #shuffle the order

colorOrderListWeek4 = np.repeat([1,2],10)
random.shuffle(colorOrderListWeek4); #shuffle the order


# make columns for condition for round1 1 and round 2 of gambling task
# where 0 = control condition
# where 1 = strategy condition

# copying the orderlist for cond1 and cond2 variables and combine the np arrays for weeks 2-4 into one
orderList_wks2_3_4 = np.concatenate((orderListWeek2,orderListWeek3,orderListWeek4))
cond1 = copy.copy(orderList_wks2_3_4)
cond2 = copy.copy(orderList_wks2_3_4)


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
colorOrderList_wks2_3_4 = np.concatenate((colorOrderListWeek2, colorOrderListWeek3, colorOrderListWeek4))

cond1color = copy.copy(colorOrderList_wks2_3_4)
cond2color = copy.copy(colorOrderList_wks2_3_4)

cond1color[[i for i, j in enumerate(cond1color) if j == 1]]= 0 # green for round 1
cond1color[[i for i, j in enumerate(cond1color) if j == 2]]= 1 # purple for round 1


cond2color[[i for i, j in enumerate(cond2color) if j == 2]]= 0 # green for round 2 (don't need to change 1 because that already means purple is second)


tmpdataWks_2_3_4 = {
  "condCode": orderList_wks2_3_4,
  "subID": subIDlistWeeks2_3_4,
  "cond1": cond1,
  "cond2": cond2,
  "cond1color": cond1color,
  "cond2color": cond2color
}

week2_3_4_DF = pd.DataFrame(tmpdataWks_2_3_4)




# combine the three dataframes: conditions completed, week 1 ,and weeks 2-4

frames = [completeCondFileFull,week1DF, week2_3_4_DF] # a necessary step to combining the pd dataframes
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

bigDF.to_csv("rcsConditionsUpdated_Winter.csv", index=False) # save the csv file

