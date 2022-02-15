# This script creates the choice set for the risk, context and strategy study
# Hayley Brooks
# 2/10/22

#clear environment
rm(list=ls())


# configuration
library('config')
config = config::get()


# TRIAL TIMING FEATURES
# choice display = 2s, decision window = 2s, isi = .5s, outcome = 1s, iti = c(1s, 1.5s, 2s)
# possible trial lengths = 6.5s, 7s, 7.5s
# avg trial length = 7s
# if we want the task to be 15 minutes long, we can get roughly 128 trials 


# STRUCTURE OF CHOICE SET
# The goal is to keep as many features as possible from previous choice set versions (specifically VNI/CAP), shorten the length, while retaining statistical power and precision.

# In VNI, the number of runs/shifts was a direct function of the number of levels, and our desire to fully cross them. There are 21 runs in VNI because there are 5 levels and we wanted to make sure every level shifted to every other level evenly (which req. 20 + 1 so the starting one is shifted to the final time time; we get there by: 5 levels; each needs to go to the other 4 levels one time, so we need a total of 5*4 shifts, which requires 5*4+1 runs).

# To start (for parameter recovery):
# 3 levels (5, 15, 25 EV) --> 12 shifts with 13 runs, 4 runs/level, with one happening an extra time
# 42 trials per level with run lengths 5, 5, 16, 16, and the last run that we add on will have 5 trials
# four runs/level means that each run is fully crossed twice
# total trials will be 131 








