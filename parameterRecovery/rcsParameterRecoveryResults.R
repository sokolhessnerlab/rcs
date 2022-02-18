# Look at parameter recovery success for basic PT model for rcs choice set

load("/Users/hayley/Documents/GitHub/rcs/parameterRecovery/parameterRecoveryOutput.Rdata")

nSub=dim(PTparRecResults)[1];
iter=dim(PTparRecResults)[3];
PTvals = matrix(data = NA, nrow=nSub, ncol = 2, dimnames = list(c(NULL), c( "rho", "mu"))); 
PTvals[,1] = rep(c(.5, .65, .9, 1.1, 1.5), each=5); # rho 
PTvals[,2] = rep(c(60,90,120,150,180), times=5); # mu 


#rho:
goodcount = 0
badcount =0
for(s in 1:nSub){
  for(i in 1:iter){
    if(!is.nan(PTparRecResults[s,3,i])){
      lowCI = PTparRecResults[s,1,i] - (2*PTparRecResults[s,3,i]); # low CI
      upCI = PTparRecResults[s,1,i] + (2*PTparRecResults[s,3,i]); # high CI
      if(PTvals[s,1] >= lowCI && PTvals[s,1] <= upCI){
        goodcount = goodcount + 1
      } else{
        print(c(s,i)); # print the subs and the iteration that was not successful
        badcount = badcount+1
      }
    }else{
      print(c(s,i,'nan'))
    }
  }
}



#mu:
goodcount = 0
badcount = 0
for(s in 1:nSub){
  for(i in 1:iter){
    if(!is.nan(PTparRecResults[s,4,i])){
      lowCI = PTparRecResults[s,2,i] - (2*PTparRecResults[s,4,i]); # low CI
      upCI = PTparRecResults[s,2,i] + (2*PTparRecResults[s,4,i]); # high CI
      if(PTvals[s,2] >= lowCI && PTvals[s,2] <= upCI){
        goodcount = goodcount + 1
      } else{
        print(c(s,i)); # print the subs and the iteration that was not successful
        badcount = badcount+1
      }
    }else{
      print(c(s,i,'nan'))
    }
  }
}



for(s in 1:nSub){
  for(i in 1:iter){
    cs = rcsChoiceSet(); # generate a new choice set; activate the choice set function in vniChoiceSet.R
    predictP = conLprob(PTvals[s,], cs); #USING THE conLprob FUNCTION IN shlab/Projects/CBM/code/cbmPT.R (constrains lambda to 1)
    choice = vector(); # temporarily store choices generated from predicted probabilities
    
    rn = runif(nrow(cs),0,1); # create a random number for each trial
    choice[predictP > rn] = 1; #if random number is less than predicted prob, set choice to 1 --> gamble
    choice[predictP < rn] = 0; #if random number is more than predicted prob, set choice to 0 --> no gamble
    
    yvals = seq(from=0,to=55,by=5);#  gain values
    rho = PTvals[s,1]; 
    xvalsSeekingL = (0.5*(yvals^rho))^(1/rho); # when the utili
    
    plot(cs$alternative, cs$riskyGain, col=choice/.5+2, main=sprintf("choices for rho = %g, mu = %g\n iteration %g", PTvals[s,1], PTvals[s,2], i)); # blue is accept, red is reject
    lines(xvalsSeekingL,yvals, col='green',lty = "longdash"); # add line for rho = 1.5
    
    segments(0,20,10,0, lwd=1); # slope = -2, intercept = 20
    segments(5,30,15,10, lwd=1); # slope = -2, intercept =40
    segments(10,40,20,20, lwd=1); # slope = -2, intercept = 60
    segments(15,50,25,30, lwd=1); # slope = -2, intercept = 80
    segments(20,60,30,40, lwd=1); # slope = -2, intercept = 100
  }
}