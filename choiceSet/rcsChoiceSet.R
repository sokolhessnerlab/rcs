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
# if we want the task to be 15 minutes long, we can get roughly 128 trials (I think we should aim for no more than this or even less if possible)


# STRUCTURE OF CHOICE SET
# The goal is to keep as many features as possible from previous choice set versions (specifically VNI/CAP), shorten the length, while retaining statistical power and precision.


# 1) Levels of context (i.e. expected value; VNI: 5 levels: 5,10,15,20,25 EV)
# 2) Shifts  (up and down) that occur systematically within each choiceset  (VNI: 21 shifts)
# 3) Roughly 128 trials (VNI: 219 trials)
# 4) runs of trials with varying lengths (VNI: 6, 9, 12, 15 trials + extra run of 9 trials for starting/ending level)

# POSSIBLE CHOICE SETS FOR RCS:

# scenario 1: 3 levels (5, 15, 25), keep 4 runs per level with same trial length = 126 trials + extra run (e.g. 6 trials)
#   - 132 trials; with trial lengths being 6.5, 7, and 7.5s, this would be 15.4 minutes
#   - this preserves *most* of the choice set structure as before.
#   - this is my preferred starting point.

# Some other scenarios include (there are many possibilities - these just seemed most reasonable in my head):
# scenario 2: 3 levels (5, 15, 25), 3 runs per level with 6, 9, 12 run lengths = 81 trials + extra run
# scenario 3: 3 levels (5, 15, 25), 3 runs per level with 9, 12, 15 run lengths = 108 trials + extra run
# scenario 4: 5 levels (5, 10, 15, 25), fewer runs per level (e.g. 3) with 6, 9, 12 run lengths = 135 trials + extra run
# scenario 5: 5 levels (5, 10, 15, 25), fewer runs per level (e.g. 3), keeping small and large (6 and 15 trials) run lengths = 105 trials + extra run




