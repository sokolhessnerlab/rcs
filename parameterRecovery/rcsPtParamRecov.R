# Function for the parameter recovery exercise
# sets up bounds, initiatl parvals, optim, etc.

rcsPTparRec <- function(n,subjdata){
  alloutput <- list() # Prepare the object into which we're going to put all the outputs of each iteraction
  for(i in 1:n){ # n is iteration for each core
    lb = c(.01,.01); 
    ub = c(2,220); 
    initparval =  c(runif(1,.01,1.2),runif(1,.02,20))
    alloutput[[i]] <- NA
    try({output = optim(initparval, conL, choiceset=subjdata, method= "L-BFGS-B", lower=lb, upper=ub,hessian=TRUE); #using conL function
    alloutput[[i]] <- output}); # Save the output into a bigass list
  };
  return(alloutput) # return big list
};
