#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 04:51:26 2022

@author: shlab
"""


import pandas as pd

# At this point, we have 79 participants (excluding 5) and the goal is to get another 80 or so.
# The condition file as is, is not evenly weighted by when we get certain conditions (lots of 1 and 4 conditions but much less 2 and 3s)
# We are going to update the condition csv so that after each week (or roughtly 20 people), we have a similar number of people in each group



# import the conditions file
# this condition file has 125 rows where the excluded participant condition codes have been added to the end
# we originally planned for 120 participants but will now be going for 160
condFile = pd.read_csv('/Users/shlab/Documents/GitHub/rcs/task/rdmTask/rcsConditions.csv')





nSubComplete = 79 
subIDExclude = [12,15,22,28,67] 


# Data collection part 2 (winter quarter)
# week 1 (20 people)


# calculate number of conditions we have completed so far (excluding the exclusions)
# then calcaute the number of ecah condition we need in the first week to even out number of poeple in the groups
# then for the following weeks or set of 20 people, then it should be 5 participants per condition.