# RCS Analysis Notes and Summary

## For Hayley's Dissertation Project on risky decision-making, temporal context and cognitive strategies

### Study at-a-glance

In this study, participants completed two rounds of a risky decision-making task (after consent and substance use questionnaire).
Prior to each round of the task, participants were randomly assigned to receive instructions to either act natural or to ignore context (strategy) in a fully-crossed manner resulting in 4 groups: natural-natural, natural-strategy, strategy-natural, and strategy-strategy. Following each round of the decision-making task,participants reported the difficulty, and frequency of following the instructions (on a scale from 1-100 with 1 = easy or never and 100 = most difficult or all the time). Participants were shown the outcome of a randomly selected trial following each round of the task and then one
of the two outcomes were randomly selected for payment once both rounds were complete.

After participants completed the risky decision-making task, they completed two complex span tasks (the OSpan and SymSpan tasks), the Emotion Regulation Questionnaire, and a demographic questionnaire.

### Basic participant information (inc. demographic info)

-   We collected data for a total of 134 participants. After exclusion criteria was applied, we have a total of 124 participants evenly distributed across the four groups (n=31/group).

-   Across the 124 participants and both rounds we have a total 32,414 choices (after removing missed trials, more details below).

#### Exclusion across all tasks and missed trial information for RDM

-   RDM task: there are 5 predetermined exclusion criteria and participants needed to pass 4 or more to be included in all analyses. Participants were additionally excluded if they reported that their choices were influenced by other things outside of task parameters and/or made it clear that they did not understand the task (e.g. pressed both response buttons at the same time). Because the risky decision-making task is the task of interest, if participants were excluded from the RDM analysis, they were excluded from all analyses. Of the 134 participants:
    -   8 were excluded for failing criteria above
    -   2 were excluded for indicating that they did not understand task or that their choices reflected something other than values on the screen or other task parameters.

Across the 124 participants included in the analysis, there were a total of 74 missed trials (median missed trial across both rounds = 0).

#### Demographic

-   Gender: 80 female, 40 male, 1 trans male, 2 gender nonconforming, 1 other;

-   Age: mean(sd) age: 19.24(1.78) years, median age: 19 years, range:18-32 years.

-   Ethnicity: 15 hispanic or latino and 109 not hispanic or latino.

-   Race: white = 101; Black or African American = 2; American Indian and Alaskan Native = 1; Asian = 8; two or more races = 10; 2 decline to answer

-   Complex span tasks: Participants had to maintain 85% accuracy on the overall math and symmetry judgements to ensure that participants were not trading off recall accuracy with distractor accuracy. Individuals who did not maintain 85% on a given task, were only excluded from analyses involving that specific complex span task (i.e. participants were not excluded across both complex span tasks if they only failed on one of the tasks). Of the 124 participants:

    -   14 participants were excluded from SymSpan for not passing symmetry scoring criteria
    -   9 participants were excluded from the OSpan for not passing symmetry scoring criteria
    -   2 additional participants were excluded from both for not completing the tasks
    -   16 total excluded from SymSpan; 11 total excluded from OSpan; including 4 participants who were excluded from both.
    -   we have at least one complex span data point for 120 people (97%)

-   Composite complex span scores: we combined the complex span scores by normalizing each individual score by the max (25 for ospan, 14 for symspan) then took the average of the normalized scores.

### Basic RDM stats (inc. p(gamble), condition stats, post-round/task questions)

#### Probability of gambling by round/condition

-   round 1: mean = 0.5338

-   round 2: mean = 0.5343 (paired t-test shows this is not a
    significant difference)

-   Suggests there is no strong effect of round on its own.

-   Probability of gambling across round/condition: When participants
    switch conditions, there is more risk-taking after being told to
    ignore context regardless of order. There is less risk-taking over
    time for those who do natural both rounds (consistent with previous
    research, e.g. PSH 2016) and there is more risk-taking over time for
    those who do strategy both rounds.
    
![pgamByRound_condition](https://user-images.githubusercontent.com/19710394/221984145-8ddb3046-676b-4e1c-b7e6-083512f6f48f.jpg)


#### Instruction difficulty and frequency

*DIFFICULTY RATINGS: Scale from 1-100* 
- Overall, difficulty ratings ranged, on average between 27-41 across groups. The difficulty patterns are unusual/inconsistent suggesting that using such ratings or means of these ratings is not the best method. 
- When comparing natural vs. strategy as a function of previous strategy (nat-nat vs nat-strat and
strat-nat vs strat-strat), all difficulty ratings following natural instructions are higher (i.e. anything after natural is more difficult -
even nat-nat) and following strategy, the difficulty ratings are lower (i.e. everything is easier following strategy). 
**- Comparing just the first round nat vs. strat, there is no significant difference in difficulty ratings (n=62 in each group; p = .5). So in the "cleanest" analysis, we don't see an effect between the difficulty ratings in the strategy which implies the difficulty is not fundamentally different. **
- Likely can't use this variable as a covariate.

![InstDifficultyRatingPlots](https://user-images.githubusercontent.com/19710394/221983678-8fbc107a-9ca7-47e2-b1a2-fa923aedec1f.jpg)


**Instruction difficulty summary stats:**
- Natural-Natural: Difficulty ratings increased across rounds
  - round 1 mean = 27.48, range = 1-64.4
  - round 2 mean = 36.489, range = 1.76-79.6 (significant diff, p = .02)
- Natural-Strategy: Difficulty ratings increased across rounds
  - round 1 mean = 31.55, range = 1-77.64
  - round 2 mean = 41.78, range = 2.64-92.58 (trending diff, p = .09)
- Strategy-Natural: Difficulty ratings were slightly lower across
rounds 
  - round 1 mean = 31.1, range = 1-99.8
  - round 2 mean = 28.30, range = 1-76.17 (n.s., p =.64)
- Strategy-Strategy : Difficulty ratings were slightly lower across rounds 
  - round 1 mean = 33.84, range = 1-87
  - round 2 mean = 30.15, range = 2.9-86.8 (n.s., p=.35)

**LMER model regressing difficulty on round and strategy shows no significant relationship between difficulty ratings and round or strategy
**

*FREQUENCY RATINGS: scale from 1 to 100* 
- Overall, participants reported following instructions 70-80% of the time. When participants repeat conditions, frequency ratings are similar. When participants switch conditions, frequency ratings are higher for natural relative to strategy condition but this difference is only significant when going from natural to strategy. There was no significant difference between natural and strategy frequency ratings for people who do natural and strategy first (i.e .when just looking at round 1 data; n=62 each group). 
**- This lines up with story from difficulty - these two conditions don't really vary in terms of their subjective difficulty and how often they can implement the strategy.**

**Instruction frequency summary stats:**

- Natural-Natural: ratings roughly the same across rounds (means~73) 
  - round 1 mean = 73.10, range = 18.36 - 98.73
  - round 2 mean = 72.31, range = 38.18 - 97.66 (n.s. p = .8)
- Natural-Strategy: frequency rating less in strategy condition 
  - round 1 mean = 76.87, range = 48.44 - 99.71
  - round 2 mean =  69.22, range = 22.17 - 99.9 (significant, p =.04)
- Strategy-Natural: frequency rating less in strategy condition 
  - round 1 mean = 76.97, range = 31.05 - 99.12
  - round 2 mean = 78.4, range = 38.77 - 99.9 (n.s., p = .7)
- Strategy-Strategy: ratings less in round 2 
  - round 1 mean = 79.69, range = 35.84 - 98.54
  - round 2 mean = 74.36, range = 25.78 - 99.02 (n.s., p=.15)
  
**LMER model regressing frequency on round and strategy shows no significant relationship between frequency ratings and round or strategy
**

![InstFrequencyRatingPlots](https://user-images.githubusercontent.com/19710394/221984537-b270cc7a-c932-4582-a699-65b21cbaa18a.jpg)

*REACTION TIMES:* 
- We looked at reaction time in a few ways, using 1) mean of mean, 2) mean of means with fast trials (<1s) removed, 3) mean of medians, and 4) mean of medians with fast trials (<.5s) removed (14 fast trials across 9 participants in round 1 with a single sub having at most 4 of these trials, 7 fast trials across 6 participants in round 2 with a single sub having at most 2 of these trials)
- We also tested removing trials with RTs <1s which included 7600 trials overall. Each of the 124 participants had at least one of these trials and for some this number of trials was in the 100s. The results are consistent with the analyses reported below for all trials and fast trials removed (RTs<.5s)

-   Overall (across the 4 types of analyses), participants were faster in round 2 relative to round 1 regardless of strategy/order. Looking
    in just round 1 data (nat vs strat, n=62), there were no significant differences in RT by instruction type.
-   **This is also consistent with our takeaways above that the strategy and control conditions take similar resources to implement and experiences are similar across instructions.**

Plot below is mean of median RT plotted for round 1 vs round for each condition:
    ![medianRTAcrossRndsStratPlotsNoFastTrials](https://user-images.githubusercontent.com/19710394/221986838-86d2f596-2b08-4325-ad95-2b055230ae6d.jpg)

-   Increase speed over rounds is likely practice effect at assessing the values. Plot below shows mean RT within each round. Sharpest decrease in RT occurs in first round and slightly decreases across round 2.
![meanRTacrossrounds](https://user-images.githubusercontent.com/19710394/221962030-11844faa-781c-4357-b5cb-615f7b1c3ad3.png)

_Note: not removing these fast trials from all analyses because they could be indicative of contextual effects (e.g. people getting faster as a result of context)_

#### Post-task questionnaire: Motivation and perceived RDM round indepedence

-   MOTIVATION: people were generally motivated during the experiment with mean ratings = 5.17 (range = 2-7 on a scale from 1-7). No big difference in motivation across conditions.

![MotivationHist](https://user-images.githubusercontent.com/19710394/221989751-5825227a-e160-4e59-9de6-6d859f7ab2b2.jpg)


-   ROUND INDEPENDENCE (i.e. how independent did the rounds feel?): participants felt the rounds generally felt independent (mean = 4.992; median = 5,
    range = 1-7 on a scale from 1-7). 
    
    ![RDMroundIndepHist](https://user-images.githubusercontent.com/19710394/221989842-d99b8e61-5749-43ce-9619-66528d6c0f76.jpg)

-   Differences in ratings of independence depending on condition.
    - Natural-Natural mean = 4.48 
    - Natural-Strategy mean = 5.355
    - Strategy-Natural mean = 4.871 
    - Strategy-Strategy mean = 5.258
    - Histograms of independence ratings show that when people switch conditions, they tend to rate independence as higher. Lots of variability when repeating natural. Barely anyone rates low indepenence in strat-strat (makes sense given instructions to ignore previous stuff)
    
![RDMroundIndepByCondition](https://user-images.githubusercontent.com/19710394/221989879-f4dfecfb-de01-4c3b-8d8e-4acbc2a57a85.jpg)

### Basic complex span tasks stats

- OSPAN: range = 0-25; mean =14.53; median = 13 
- SYMSPAN: range = 0-14; mean = 7.657; median = 9 
  - Ospan and symspan are correlated: r = .26, p = .009 
- COMPOSITE: range = .06 - 1; median = .5743; mean = .57. 
  - Wide variation in composite scores - good for individuals variability.
  - 
![compositeSpanScoreHist](https://user-images.githubusercontent.com/19710394/221991618-32ba8264-bfd9-44db-b213-40f35851766e.jpg)

To do:
- Test the correlation coefficient with Foster et al paper with N=589, r = .53 with our correlation here.

_**To what extent is the scoring on these complex span capturing capacity or motivation?**_
We cannot totally rid this possibility, but the data supports that the composite span is a measure of capacity over motivation. They are all achieving the same baseline level of math performance (85% or higher). Not a correlational relationship between motivation and composite span.


### Basic ERQ stats

- ERQ REAPPRAISAL: range = 14-42; mean = 29.69; median = 30 
- ERQ SUPPRESSION: range = 4 - 27; mean = 14.89; median = 15
- No correlation between reappraisal and suppression, p = .4

![ERQHist](https://user-images.githubusercontent.com/19710394/221994792-271a7b1c-3488-4f83-907e-1009fc8e1a6e.jpg)

-   How does the complex span and ERQ compare to other studies?

### Individual-level measures: Are they related?

1. **Is ERQ related to composite span?** No relationship between ERQ suppression and composite span or ERQ reappraisal and composite span.
2. **Is ERQ related to motivation?** We don't expect a relationship, but we are thinking these could both be related to strategy effectiveness and want to ensure these are different things. There is not relationship between reappraisal score and motivation but there is a negative relationship between suppression and motivation (i.e. higher suppression score was associated with lower motivation). Unclear what this means because we didn't have a hypothesis or expectation about this.
3. **Is capacity related to motivation** We don't see a correlation between capacity and motivation.
4. **Is instruction difficulty and frequency related to ERQ, composite span, or motivation?** 
    - Looked at this several ways, each in linear models. 
        - No main effects of composite span, ERQ, and motivation on instruction difficuly and frequency.
        - For difficulty ratings, no interaction with indiv. measurements and strategy.
        - For frequency ratings, main effect of strategy, interation with strategy and motivation. The effects are such that 1) people follow instructions more in strategy condition relative to act natural and 2) when motivation is low, frequency ratings are higher in strategy than natural and vice versa (this doesn't take round into consideration)
        - Accounting for round in a few ways (e.g. used condition code = 1,2,3,4 and then split up data by round). **The takeaway seems to be that the effect of motivation on frequency is negative for strategy condition and is positive for natural condition. High motivation is good for following act natural instructions but bad for following strategy instructions.**

In general, these individual-level measures appear range widely across people which is great for capturing the effects of these measures. Complex span, motivation and ERQ also appear to be capturing different things, but will note relationship between suppression and motivation.


## Temporal context effects!

### Generalized linear mixed effects modeling

#### Risky decision-making analysis

Trial-level model: Accounting for option values, magnitude, strategy and
round

People are more likely to choose an option as it gets bigger and gamble
less as values increase overall. Risk-taking increases in the strategy
relative to natural condition and this effect is strongest in round 2.

        Fixed effects:
                                    Estimate Std. Error z value Pr(>|z|)    
        (Intercept)                 -0.05629    0.10096  -0.558  0.57717    
        gainScaled                  12.59125    0.68694  18.330  < 2e-16 ***
        safeScaled                 -16.07157    1.34337 -11.964  < 2e-16 ***
        evLevScaled                 -8.23973    2.66697  -3.090  0.00200 ** 
        roundRecode                 -0.00704    0.01407  -0.500  0.61673    
        strategyRecode               0.09960    0.01990   5.006 5.56e-07 ***
        roundRecode:strategyRecode   0.05627    0.01951   2.885  0.00392 ** 
        AIC = 31127.6
        
**Effect size for round x strategy on risk-taking**
        
![pgamRoundxCondition](https://user-images.githubusercontent.com/19710394/222292947-ef09e884-71f7-4a78-8fbe-e53115e65a9c.jpg)


#### Do we see effects of past outcome, positive shift and earnings relative to expectations?
- For this analysis, we used generalized linear models regressing choice on to three timescales: past outcome, shift and earnings relative to expectations. For this analysis, signed shift outperformed models including separate regressors for positive and negative shift and there was no interaction between earnings and linear expectations. Unlike some previous datasets, past outcome interacts with both earnings and expectations. The two best fitting models are described below. Like previous datasets, the shift effect is short-lasting and drops off right after a trial following a shift.
- 
- Two base models (best-fitting by AIC; generalized linear models - no mixed effects, model is singular and shows no ranef)
1) Base model 1: past outcome amount, signed shift amount, earnings and expectations
    - all main effects are significant in direction that we would expect: 
    
            Coefficients:
                                       Estimate Std. Error z value Pr(>|z|)    
            pastOC1sc             -0.17555    0.04955  -3.543 0.000396 ***
            signedShiftsc          0.51615    0.20202   2.555 0.010622 *  
            earnNormalizedOverall  1.20453    0.25269   4.767 1.87e-06 ***
            linExpectation        -0.86596    0.20621  -4.199 2.68e-05 ***
            
            AIC = 30226
**Plots below show effect sizes for each timescale for model results right above**
![model_pocSignedShiftEarnExp_pocES](https://user-images.githubusercontent.com/19710394/222309223-d38ad075-7786-4975-9fbb-e5ef8958a297.jpg)
    
![model_pocSignedShiftEarnExp_shiftES](https://user-images.githubusercontent.com/19710394/222310747-6371799c-209d-474c-87d4-78736646de26.jpg)

![model_pocSignedShiftEarnExp_earnExpOnPgam](https://user-images.githubusercontent.com/19710394/222310759-55a69e84-f8b7-42b7-b476-e3d184d63c08.jpg)

    

2) Base model 2: past outcome amount, signed shift amount, earnings and expectations with interaction between past outcome and earnings and past outcome and expectations.
    - main effects of past outcome, signed shift remain and interaction between poc x expectation and poc x earnings. No main effects of linear expectation and earnings. 
    - Interaction between poc and earnings: negative effect of outcome becomes stronger with increased earnings
    - Interaction bewteen poc and expectatatins: negative effect of outcome flips and becomes positive with increased expectations

            Coefficients:
                                            Estimate Std. Error z value Pr(>|z|)    
            pastOC1sc                       -0.34588    0.07866  -4.397  1.1e-05 ***
            signedShiftsc                    0.53988    0.20222   2.670  0.00759 ** 
            earnNormalizedOverall            0.27013    0.35897   0.753  0.45174    
            linExpectation                  -0.14877    0.29185  -0.510  0.61023    
            pastOC1sc:earnNormalizedOverall  3.42749    0.96449   3.554  0.00038 ***
            pastOC1sc:linExpectation        -2.39657    0.79483  -3.015  0.00257 ** 
            
            AIC = 30211
            
**Plots below show effect sizes for each timescale for model results right above**

![model_pocSignedShiftEarnExp_pocIntxns_pocES](https://user-images.githubusercontent.com/19710394/222311955-a6b1c95a-5c88-4f3f-9604-303412bdc3dd.jpg)
![model_pocSignedShiftEarnExp_pocIntxns_shiftES](https://user-images.githubusercontent.com/19710394/222311702-5fa1d3c8-6026-437d-bc76-8ab24dcbb5ef.jpg)
![model_pocSignedShiftEarnExp_pocIntxns_pocEarnExpES](https://user-images.githubusercontent.com/19710394/222311733-66d4aaa1-26f2-414e-918f-c1a431b06e82.jpg)



#### Does strategy and/or round interact with the three timescales?
Because we found an interaction between strategy and round in our trial-level model, we tested interactions between strategy and each of the temporal context effects in our two base models.

**Base model 1 x Strategy (and round)**
- The best fitting model with strategy and base model 1 includes an interaction between strategy and EACH level of context: past outcome, signed shift, linear expectation and earnings. Adding strategy to each level improved model fit (AIC = 30225) and showed trending interactions between strategy x past outcome and strategy x signed shift. These trending effects are that the negative past outcome is weaker in strategy condition and the signed shift effect is stronger in the strategy condition.
- Accounting for round did not improve model fit but did show an trending interaction between signed shift x strategy x round. In this model, it seems like the big 3-way interaction means that in round 1, there is no effect of strategy on signed shift but in round 2 the effect of signed shift is negative for act-natural condition and is positive for strategy condition.

**Base model 2 x Strategy (and round)**
- The best fitting model with strategy and base model 2 includes strategy interacting with past outcome and signed shift (but not with pocxexp and pocxearn). The trending interaction between past outcome x strategy and signed shift x strategy are consistent with results above (strategy weakens poc and strengthens shift effect).
- Adding round made AIC worse but there were a lot of additional interactions with round, including:
    - round x earnings and round x expectations with these effects weakening in round 2
    - round x earnings x poc and round x expectations x poc
    - big 4-way interactions: round x earnings x poc x strategy and round x expectations x poc x strategy
**- Questions: Is this is saying something about how people are treating earnings and expectations across rounds? Should we be accounting for people who repeat vs. switch conditions and how they may differentially treat rounds of the risky decision-making task. Should we just look at round 1 data for the cleanest analysis? Also, the impact of round x strat x poc and exp/earnings does indicate that these things are potentially related as we believe (mechanistically).**


#### Temporal context effects, strategy and round in people who switch vs. repeat conditions.
- For the following analysis, we split up the data to include people who switched conditions (n=62) and people who repeated conditions(n=62). The rationale is that 1) people who switch/repeat conditions report different perceptions of task independence and 2) the finding that strategy is stronger in round 2 suggests that repeated exposure to strategy may be increasing its strength on risk-taking (i.e. for people who do repeat the same strategy each round of the rdm task).
- For these analyses, we used the same two base models as above, adding round and strategy to each model.
- For both groups, there is more risk-taking in the strategy condition but round only makes the effect of strategy stronger for people who repeat conditions. This suggests that spending more time with instructions, increases their influence on risk-taking.
- Both groups show contextual effects of past outcome, earnings, and expectations (base moddel 1) as well as poc x earnings and poc x expectations (base model 2) but only the group that switches conditions has a main effect of signed shift.
- Temporal context effects interact with strategy/round ONLY for people who repeat conditions. 
    -  For people who repeat conditions, strategy makes shift effefct stronger but weakens earning and expectation effect. Strategy does not significantly interact with past outcome (p=.13) but the direction of the interaction is consistent with strategy weakening the past outcome effect. Treading lightly here because of n.s. results -> the pattern of interactions in people who repeat instructions is that strategy weakens immediate and global timescales but strengthens neighborhood timescale.
    - This is consistent with the pattern that strategy/instructions are stronger in round 2 (perhaps after more experience with those instructions) and for people who switch, they may not experience the same impact of instruction as those who repeat instructions.

- Re: round x global timescale we see in models above for people who repeat conditions - could this be that people who repeat conditions track earnings and expectations across rounds?
    - Yes, for people who repeat conditions, global timescale effect appear to span both rounds but that this effect is weaker for people doing the strategy condition both rounds but people who switch conditions appear to track earnings and expectations within rounds. This is consistent with round independence ratings (people who repeat natural are more likely to say rounds did not feel independent where as people who repeat strategy are more likely to say rounds felt independent).


#### Temporal context effects and strategy in ROUND 1 data only
 - For this analysis, we just looked at choices made in round 1 (n=124, 62 per strategy). This is considered the "cleanest" analysis because there are no order effects, but we lose power/ability to comapre within subjects.
 - We used the same two base modes as abaove, adding strategy to each model:
 - At the trial level, there is no effect of strategy on choice in round 1.
 - Past outcome effect is strong across both base models, signed shift is less consistent but trending, and interacting poc with exp and earn improves the model but the interactions are not significant nor are main effects in base model 2.
 - No effect of strategy on temporal context for people in round 2.
 - That there is no effect of strategy as a function of removing round 2 really suggests a strong relationship between strategy and round - that you can't have strategy effect without round and that the strength of strategy across time is where we really see its effects.

#### Strategy x indidivual-level measures 
For this analysis, we will use both base models (1: poc, shift, earn, exp; 2: poc, shift, earnxpoc, expxpoc). 
We will account for strategy x temporal context interactions in base model 1 by including an interaction with strategy at each timescale because this was the best performing model and in base model 2 by interacting strategy with past outcome and shift because that was the best performing base 2 model.

Does ERQ, composite span and/or motivation influence risk-taking or interact with strategy overall?

1. Trial-level model plus each individual-level variable and interaction with strategy: Only ERQ reappraisal interacts with strategy. For people with low reappraisal score, the effect of strategy is to increase risk-taking whereas for people with high reappraisal, the effect of strategy is not different natuarl condition. This demonstrates that our strategy instructions have reappraisal components and people who have a tendency to reappraise may behave naturally in a similar way to the "ignore context" instructions.

2. Looking at ERQ, span and motivation in contextual models (instead of trial-level model, still only interacting these variables with strategy-only and not temporal context variables): Only reappraisal interacts with strategy and there are not effects of the other individual-level measures on risk-taking or on strategy. The interaction bewteen ERQ and strategy in the contextual model is that for people with low reappraisal, there is no effect of strategy on risk-taking but in people with high reappraisal, strategy is associted with decreased risk-taking and natural is associated with increased risk-taking. This is different from the results in trial-level model. These results are the same across base model 1 and base model 2.

#### Strategy x individual-level measures x temporal context

For this analysis, we will use both base models that we've worked through above. We will account for strategy and temporal context as in the previous section (base model 1: poc x strat, shift x strat, earn, exp, strat x reap; base model 2: poc x strat, shift x strat, poc x earn, and poc x exp, strat x reap). These models are run only on contextual models because we are interested in how ERQ interacts with strategy's effects on temporal context

1. Base model 1: 29755 

                Coefficients:
                                                      Estimate Std. Error z value Pr(>|z|)    
                pastOC1sc                            -0.471837   0.226254  -2.085 0.037030 *  
                strategyRecode                        0.347209   0.117510   2.955 0.003130 ** 
                ERQreappSC                           -0.055687   0.044156  -1.261 0.207260    
                signedShiftsc                         0.513638   0.203925   2.519 0.011777 *  
                earnNormalizedOverall                 1.232381   0.259602   4.747 2.06e-06 ***
                linExpectation                       -0.838492   0.219144  -3.826 0.000130 ***
                pastOC1sc:strategyRecode             -0.889760   0.315255  -2.822 0.004767 ** 
                pastOC1sc:ERQreappSC                  0.458704   0.318859   1.439 0.150269    
                strategyRecode:ERQreappSC            -0.605659   0.159275  -3.803 0.000143 ***
                strategyRecode:signedShiftsc          0.314368   0.203957   1.541 0.123233    
                strategyRecode:earnNormalizedOverall -0.005748   0.259654  -0.022 0.982339    
                strategyRecode:linExpectation         0.126167   0.219644   0.574 0.565687    
                pastOC1sc:strategyRecode:ERQreappSC   1.378273   0.437217   3.152 0.001619 ** 

2. Base model 2: AIC = 29743

                Coefficients:
                                                     Estimate Std. Error z value Pr(>|z|)    
                pastOC1sc                           -0.608928   0.232937  -2.614 0.008945 ** 
                strategyRecode                       0.393028   0.114922   3.420 0.000626 ***
                ERQreappSC                           0.006207   0.055427   0.112 0.910838    
                linExpectation                      -0.190995   0.312338  -0.612 0.540868    
                signedShiftsc                        0.519049   0.203974   2.545 0.010938 *  
                earnNormalizedOverall                0.315746   0.368696   0.856 0.391784    
                pastOC1sc:strategyRecode            -0.857946   0.315981  -2.715 0.006624 ** 
                pastOC1sc:ERQreappSC                 0.359618   0.325627   1.104 0.269425    
                strategyRecode:ERQreappSC           -0.586896   0.159491  -3.680 0.000233 ***
                pastOC1sc:linExpectation            -2.475164   0.826006  -2.997 0.002731 ** 
                strategyRecode:signedShiftsc         0.305350   0.203121   1.503 0.132764    
                pastOC1sc:earnNormalizedOverall      3.540305   0.985675   3.592 0.000328 ***
                pastOC1sc:strategyRecode:ERQreappSC  1.345567   0.438310   3.070 0.002141 ** 


#### Risky decision-making, strategy and complex span
 - Because working memory capacity is associated with increased ability to exert control (hypothesized to influence strategy success here), we expect to see that higher complex span scores should interact with strategy's effects on temporal context.

#### Risky decision-making, strategy and motivation
- Because motivation can influence and/or offset capacity for control, we expect that higher motivation will directly interact with strategy and/or capacity to influence temporal context effects. 
- 
#### Risky decision-making, strategy and ERQ
- Strategy is asking people to take a new perspective, we may see a positive relationship between ERQ reappraisal scores and strategy effectiveness.
- Because strategy is asking people to ingore context as the new perspective, we may also see a positive relationship between ERQ suppression and strategy succeses. 


#### Risky decision-making, strategy, and other variables (e.g. RT)?

### Individual-level analyses

