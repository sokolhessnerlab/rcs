# This script creates the choice set for the risk, context and strategy study
# Hayley Brooks
# 2/10/22


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


rcsChoiceSet <- function(){
  
  library("plotrix")
  
  lnslope = -2; # slope of the x-y coordinates 
  
  nT = 126; # 42 trials per level (not including the extra 5 trials)
  EVlevels = seq(from=5, to= 25, by=10); # levels
  nEVLevels = length(EVlevels); # number of levels
  nPts = nT/nEVLevels; # the number of trials per level
  
  # create the dataframes where we will store the x (safe) 
  evPointsX = as.data.frame(matrix(data=NA,nrow=nPts, ncol=nEVLevels, dimnames = list(c(NULL), c("level5", "level15", "level25")))); 
  
  # setting up the "distribution":
  middleTrials = nPts*(2/3); # number of trials that are sampled in the middle (near indifference when rho=1)
  edgeTrials = (nPts*(1/3))/2; # number of trials that are sampled on the edges (away from indifference; divided by 2 because these trials are split between sides)
  
  #set x-value points to hit along the three levels:
  evPointsX$level5 = c(seq(0,3, length.out = edgeTrials), seq(3.1,6.9,length.out = middleTrials), seq(7,10, length.out = edgeTrials));
  evPointsX$level15 = c(seq(10,13, length.out = edgeTrials), seq(13.1,16.9,length.out = middleTrials), seq(17,20, length.out = edgeTrials)); 
  evPointsX$level25 = c(seq(20,23, length.out = edgeTrials), seq(23.1,26.9,length.out = middleTrials), seq(27,30, length.out = edgeTrials));
  
  # flip each column upside down  and double the values for our Y (risky gain values) coordinates
  evPointsY = apply(evPointsX, 2, rev)*-lnslope; 
  
  # add noise by creating a matrix of noise that will be applied to our evPointsX and evPointsY matrices
  
  # from a uniform distribution spanning 0 from -.5 to .5, pick 2 values, multiply by 10, round to 1 digit and divide by 10 to get 2 decimals
  addNoiseX =  matrix(data = round(runif(nPts*nEVLevels, min = -.5, max = .5)*10, digits = 1)/10, nrow = nPts, ncol =nEVLevels); 
  addNoiseY = addNoiseX*2;
  
  evPointsXnoise = round(evPointsX + addNoiseX, digits =2)
  evPointsYnoise = round(evPointsY + addNoiseY, digits =2)
  
  # adding noise may create negative values, make those zero (note that this changes some risky gain value and safe values to zero)
  evPointsXnoise[evPointsXnoise<0] = 0;
  evPointsYnoise[evPointsYnoise<0] = 0;
  
  
  
  
  
  # Now we use a matrix to make sure we hit all the EVs
  
  resample <- function(x,n) x[sample.int(length(x),n)];
  
  n = 0;
  
  while (1) {
    n = n + 1;
    mtx = matrix(data=1,nrow=3,ncol=3);
    
    for(r in 1:3){
      mtx[r,] = r;
      mtx[r,r] = NA;
    }
    
    EVs = c();
    for (i in 1:6){
      if (i == 1){
        EVs[i] = sample.int(3,1); #pick a column
      }else{
        EVs[i] = evnxt; #new column
      }
      if (i < 6){
        if (!any(which(! mtx[,EVs[i]] %in% NA))){
          break
        }
        evnxt = resample(which(! mtx[,EVs[i]] %in% NA),1);
        mtx[evnxt,EVs[i]] = NA;
      }  
      if (all(is.na(mtx[,EVs[1]]))){
        mtx[EVs[1],] = NA;
      }
    }
    if (i == 6){
      break
    }
  }
  
  EVs = c(EVs,EVs,EVs[1]); # repeat twice, then add the first EV so its fully crossed.
  
  mtx; # should be all NAs
  EVs; # should show each EV level four times, and five times for the starting EV level
  sort(diff(EVs)); # should be: -2 -2 -1 -1 -1 -1  1  1  1  1  2  2
  n;
  
  
  # each level of EV will have 2 different run lengths that occur twice (5, 5, 16, 16) for 42 trials
  # we need a 13th run because we will be going back up or down to the first run, so we will add 5 more trials evenly spaced on the final EV level seq(from = 1, to = 42, by = 9) =  c(1,10,19,28,37)
  # the only difference across people for the LAST run is that they will be at different EV levels but run length and index on the EV level will be the same.
  
  
  # translate EVs (1-5) into the actual EVs (5-25)

  realEvs = EVs;

  realEvs[realEvs==3] = EVlevels[3];
  realEvs[realEvs==2] = EVlevels[2];
  realEvs[realEvs==1] = EVlevels[1];
  
  # allocate run lengths
  rL= c(5,16);
  
  n = 0;
  while (1) {
    n = n+1
    
    runLength= vector();
    
    runmtx = matrix(data=rep(c(5,16), times=3),ncol = length(rL), byrow = TRUE);
    
    for (i in 1:6){ # for the first 6 EVs 
      
      selectRow = EVs[i]; # row is the first EV
      selectCol = resample(which(! runmtx[selectRow,] %in% NA),1);
      runLength[i] = runmtx[selectRow, selectCol];
      runmtx[selectRow,selectCol] = NA;
    }
    
    if (i == 6){
      break
    }
  }
  runLength=c(runLength,runLength,5);
  
  
  
  nTri = sum(runLength);
  nRuns = length(runLength);
  
  
  # TRIAL TIMING FEATURES
  # choice display = 2s, decision window = 2s, isi = .5s, outcome = 1s, iti = c(1s, 1.5s, 2s)
  # possible trial lengths = 6.5s, 7s, 7.5s
  # avg trial length = 7s
  # if we want the task to be 15 minutes long, we can get roughly 128 trials 
  
  itiTimes = c(1, 1.5, 2);
  itiDistTimes =itiTimes^-1.05;
  itiDistTimes = round(nTri*itiDistTimes/sum(itiDistTimes), digits = 0); # number of times we see 1, 1.5, 2 (61 40 30)
  ITIs = c();
  for (i in 1:3){
    ITIs = c(ITIs, rep(itiTimes[i],itiDistTimes[i]));  
  }
  
  ITIs = sample(ITIs);
  
  # distribute everything to the choice set
  rcsCS = as.data.frame(matrix(data = NA, nrow = nTri, ncol=8, dimnames = list(c(NULL), c("evLevel", "evInd", "runSize", "isi", "iti", "riskyGain", "riskyLoss", "alternative"))));
  
  count = 1; # start count at trial 1
  for (i in 1:length(EVs)){
    rcsCS$evLevel[count:(count+runLength[i]-1)] = realEvs[i]; # record the ground EV for every trial
    rcsCS$evInd[count:(count+runLength[i]-1)] = EVs[i];
    rcsCS$runSize[count:(count+runLength[i]-1)] = runLength[i];
    count = count + runLength[i]; # update the count
  }
  
  rcsCS$isi = .5
  rcsCS$iti = ITIs;
  
  
  # add gains, safe and loss values such that we hit all the possible values for each level of EV given the number of trials in each run
  nTevLev = 1:42;
  valueInds = matrix(data=nTevLev, nrow=length(nTevLev), ncol=nEVLevels, dimnames = list(c(NULL), c("ev5", "ev15", "ev25"))); # create a matrix where each column corresponds to EV level and there are 42 rows (for 42 trials)
  
  
  for(n in 1:nT){
    
    selectCol = rcsCS$evInd[n]; # column is level of EV for that trial, n
    
    selectRow = resample(which(! valueInds[,selectCol] %in% NA),1); # select a row
    
    rcsCS$riskyGain[n] = evPointsYnoise[selectRow,selectCol];
    rcsCS$alternative[n]= evPointsXnoise[selectRow,selectCol];
    rcsCS$riskyLoss[n] = 0; #gain only task
    
    valueInds[selectRow,selectCol] = NA ; # replace with NA so we don't select this index again
    
  };
  
  
  sum(is.finite(valueInds)); # should be zero
  
  
  # Now add the last 5 trials: evenly spaced on the final EV level seq(from = 1, to = 42, by = 9) =  1 10 19 28 37 
  last5rowInd= sample(seq(from = 1, to = 42, by = 9));
  rcsCS$riskyGain[(nT+1):nTri] = evPointsYnoise[last5rowInd, EVs[length(EVs)]];
  rcsCS$alternative[(nT+1):nTri] = evPointsXnoise[last5rowInd, EVs[length(EVs)]];
  rcsCS$riskyLoss[(nT+1):nTri] = 0;
  
  # Add attention checks
  # We want to add two trials where risky gain is large and safe is 0 
  # Let's do this for EV levels 15 and 25 
  
  attnCheck15ind = which(rcsCS$evLevel==15 & rcsCS$riskyGain>35);
  rcsCS$alternative[sample(attnCheck15ind, 1)] = 0; # pick one of those trials and make it zero
  
  attnCheck25ind = which(rcsCS$evLevel==25 & rcsCS$riskyGain>55);
  rcsCS$alternative[sample(attnCheck25ind, 1)] = 0; # pick one of those trials and make it zero
  


  # #PLOT OUR CHOICESET NOW! - THE RISKY GAIN X ALTERNATIVE SHOULD HIT EACH POINT ON EACH EV LEVEL
  yvals = seq(from=0,to=55,by=5);#  gain values
  rho = 2; #risk seeking
  xvalsSeekingH = (0.5*(yvals^rho))^(1/rho); # when the utility of the y value is equal to utility of x value
  rho = 1.5; #risk seeking
  xvalsSeekingL = (0.5*(yvals^rho))^(1/rho); # when the utility of the y value is equal to utility of x value
  rho = 0.5; #risk averse
  xvalsAverseL = (0.5*(yvals^rho))^(1/rho);
  rho = 0.75; #risk averse
  xvalsAverseH = (0.5*(yvals^rho))^(1/rho);
  xvalsNeutral = yvals*.5;
  
  ## COMMENTING OUT PLOTTING CODE BELOW FOR GENERATING THE CHOICE SET
  plot(xvalsNeutral,yvals,type='l', xlab = "safe ($)", ylab="risky gain ($)", ylim = c(0,60), xlim =c(0,30), col="black",lty = "longdash"); #risk neutral
  
  lines(yvals,yvals,type='l', col="darkgrey",lty = "longdash"); # the limit; people will never gamble here
  lines(xvalsSeekingH,yvals,col='black',lty = "longdash"); # someone who is risk seeking
  lines(xvalsSeekingL,yvals,col='black',lty = "longdash"); # someone who is risk seeking
  lines(xvalsAverseL,yvals,col='darkgrey',lty = "longdash"); # someone who is really risk averse
  lines(xvalsAverseH,yvals,col='black',lty = "longdash"); # someone who is risk averse
  
  #draw diagnoals through the rectangles (x0, y0, x1, y1)
  segments(0,20,10,0, lwd=3, col="grey"); # slope = -2, intercept = 20
  segments(10,40,20,20, lwd=3,col="grey"); # slope = -2, intercept = 60
  segments(20,60,30,40, lwd=3, col="grey"); # slope = -2, intercept = 100
  
  
  points(rcsCS$alternative, rcsCS$riskyGain, pch=16,col=rcsCS$evLevel+6); # plot the real gains and safes
  
  # plot choice set over time
  plot(rcsCS$alternative, col=rcsCS$evLevel+6, xlab="trial", ylab="safe amount ($)", pch=16);
  plot(rcsCS$riskyGain, col=rcsCS$evLevel+6, xlab="trial", ylab="risky gain amount ($)", pch=16);
  plot(rcsCS$evLevel, col=rcsCS$evLevel+6, xlab="trial", ylab="level", pch=16);
  
  
  return(rcsCS)
  
}; # end rcsChoiceSet function

#newcs = rcsChoiceSet()



