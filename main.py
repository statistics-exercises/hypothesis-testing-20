import numpy as np
import scipy.stats 

def testStatistic( data1, sigma1, data2, sigma2 ) :
  # This function should calcualte and return the test statistic T that is 
  # described in the panel on the right.  
  

def pvalue( data1, sigma1, data2, sigma2 ) : 
  # You need to write code to determine the pvalue here.  This function will need to
  # include a call to test statistic
  
  
data = np.loadtxt("mydata.dat")
print("Null hypothesis: the expectations for the two sampled distributions are the same")
print("Alternative hypothesis: the expectations for the two sampled distribution are different")
print("The p-value for this test given the data is", pvalue( data[:,0], 2, data[:,1], 4 ) )
