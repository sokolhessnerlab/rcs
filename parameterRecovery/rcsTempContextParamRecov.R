# Function for the parameter recovery exercise for temporal context
# sets up bounds, initiatl parvals, optim, etc.

rcsTempContextParRec <- function(n,subjdata){
  alloutput <- list() # Prepare the object into which we're going to put all the outputs of each iteration
  for(i in 1:n){ # n is iteration for each core
    lb = c(-2,0,-1); # poc, shift, earnings
    ub = c(2, 10, 10);  # poc, shift, earnings
    initparval =  c(runif(1,-1.5,.5),runif(1,.5,3), runif(1,.1,2))
    alloutput[[i]] <- NA
    try({output = optim(initparval, tempContextLL, choiceset=subjdata, method= "L-BFGS-B", lower=lb, upper=ub,hessian=TRUE); #using tempContextLL function
    alloutput[[i]] <- output}); # Save the output into a bigass list
  };
  return(alloutput) # return big list
};



# 2/28
# Overall, terrible recovery for the first round. The majority of recovered values are hitting the bounds (looking at histograms)
# for past outcome, bounds are both at -.2 and .5 (over 6000 at each bound)
# for shift, ~8000 were at the lower bound .5, and ~5000 were at the upper bound of 4
# for earnings, over 16000 at the .10 bound
# going to change the range of possible values