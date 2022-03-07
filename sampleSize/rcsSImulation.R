x=rep(1:10)
g = c('a','b','c')
X = expand.grid(x=x, g=g)


b = c(2, -.1)
V1 = .5
V2 = matrix(c(.5,.05, .05, 1),2)
s = 1

model1 = makeLmer(y~ x + (1|g), fixef=b, VarCorr = V1, sigma = s, data=X)

powerSim(model1, nsim=20)



source('../parameterRecovery/binaryChoices.R'); # generate binary choices
source('../parameterRecovery/temporalContextProbChoice.R'); # probability and choice function
source("../parameterRecovery/rcsTempContextParamRecov.R"); # glm parameter recovery function
source("../choiceSet/rcsChoiceSet.R")



# 120 participants, 4 groups, binomial


triLevel = glmer(choice ~ gainSC + safeSC + grndEVscaled + (0 + gainSC + safeSC|subjectIndex), data=data, family="binomial")
data$pred = predict(triLevel, type="link")
tempContext = glmer(choice ~ poc1scaled*strategy + shiftDiffscPOS*strategy + relativeEarnings*poc1scaled*strategy + (1|subjectIndex), data=data, family="binomial")

# we want strategy to be 0 or 1 (choices were either made under the strategy or not)


# make 120 choicesets, simulate choices, add strategy to the choicesets


# create 120 participants
pocVals = seq(from=-1, to =1, length.out = 6); # past outcome estimates
shiftVals = seq(from=-3, to = 3, length.out = 5); 
earnVals = seq(from=-1, to = 3, length.out = 4); 
allVals = expand.grid(pocVals, shiftVals,earnVals);

nSub = nrow(allVals);
nTasks = 2
rcsSimData = matrix();
# create choiceset and simulate their choices, add earnings, past outcome, expectations, and strategy to the choice set
for (n in 1:nsub) {
  subData = matrix();
  for (t in 1:nTasks) {
    cs = rcsChoiceSet()
    newChoiceset = contextProbChoices(allVals[n,], cs);
    ranNum = rbinom(1, 1, 0.5); # determine if this participant was in strategy or control condition (0=control; 1 = strategy)
    newChoiceset$strategy[1:nrow(newChoiceset)] = ranNum; # save strategy in choice set
    newChoiceset$subID[1:nrow(newChoiceset)] = n # save sub ID
    newChoiceset$taskNum[1:nrow(newChoiceset)] = t; # save task iteration
    subData = cbind()
  }
}
