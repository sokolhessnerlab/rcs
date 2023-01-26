## Exclusion process for RCS

### Risky decision-making task 
(5 criteria for exclusion, participants must pass 4 or more to be included.)
 1. missed more than 10% of trials (i.e. more than 13 trials in each round)
 2. missed too many attention checks (at least 30% of attention check trials)
    - Two types of attention check trials: "should gamble" trials where risky gain is very large and safe is $0 and "should safe" trials where safe amount is more than risky gain amount
 3. pgamble is less than .05 and greater than .95 
 4. choices were not influenced by gain and safe amount (as demonstrated by individual-level glms)
 5. responses were too fast - average reaction time in each round was less than 1s. I
    - Note: one alternative is to exclude individual trials where RT was less than 1s but for participants who have an avg RT that is less than 1s, this would mean excluding a lot of trials and its unclear what this would mean for looking at temporal context effects or we could base this on proportion of trials with RTs that fall under 1s.


Exclusion by self-report is when participants indicate that they did not understand the task or that their responses did not reflect the values on the screen.

For the risky decision-making data, if a participant is excluded from one round, they are excluded across the study.

Participants that are excluded:
sub-012: technically passed exclusion criteria above (failed glm criteria) but self-reported that they pressed both response buttons at the same time to let computer select the option
sub-015: technically passed exclusion criteria above (failed glm criteria) but reported using patterns (gamble outcomes based on the side of the screen they were presented on) detected in the choice set to make their decisions
sub-022: failed 3 or more exclusion criteria above 
sub-028: failed 3 or more exclusion criteria above
sub-067: failed 3 or more exclusion criteria above
sub-105: failed 3 or more exclusion criteria above

### Complex span tasks
- Participants are excluded from analysis involving ospan or symspan if they 1) did not complete the task (see [incompleteData.md](./analysis/incompleteData.md)) or if they scored less than 85% on the overall math or symmetry problems (this is based on Englelab protocol).
- Exclusion is not applied across complex span tasks (i.e. participants are only excluded from the complex span task for which they dont pass the criteria above)

Participants that are excluded:

*both symspan and ospan*: 
  - subs-037, 082: did not complete tasks
  - sub-024: did not pass scoring criteria

*symspan*: subs-020, 028, 031, 034, 041, 050, 054, 055, 068, 071, 094 097, 111 (did not pass scoring criteria) 

*ospan*: subs-015, 018, 019, 022, 027, 057, 89 (did not pass scoring criteria)


### Emotion regulation questionnaire
- Participants are excluded from analyses involving ERQ if they did not complete it or if they missed responses.
Participants that are excluded:
 - subs-025, 061 did not respond to all questions


Each of these exclusions are available in matrix/csv form as described by this [README.md](./analysis/README.md).

