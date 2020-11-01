# Comparing means

In this exericse we want to consider how we can compare the sample means in the sub-groups of a data set.   If we are able to compare sample  means in this way we can begin to tackle questions such as:

_Are women paid less than men on average_

Questions such as the one above are much easier to explain to stakeholders as they involve "less mathematics."  By this, I mean that we do not have to explain why we think the expectation might take a certain value or say anything about the distribution that is assumed under the null hypothesis at all.  In fact, if you think about the most interesting hypothesis tests we have done thus far we have been answering questions of this type.  For the farmer with the apples from last week,  for instance, we were comparing the average weights of the apples last year with the average weights this year.  The steps the farmer would have taken to  do this test are as follows:

1. Farmer calculates sample mean (![](https://render.githubusercontent.com/render/math?math=\mu_0)) and standard deviation (![](https://render.githubusercontent.com/render/math?math=\sigma)) for apples harvested in the previous year
2. Farmer calculates sample mean for apples harvested this year.
3. Farmer performs a hypothesis test at 5% significance level assuming under the null hypothesis that the weights of the apples this year are all samples from a distribution with expectation mu0 and standard deviation sigma.

This is a bad way to perform this hypothesis test as we need to assume that the standard deviation for the weights of the apples this year is the same than the standard deviation of the weights of the apples last year.  In this exercise and the next, we are thus going to learn about a method for testing hypotheses such as this without making assumptions about the equality of the standard deviations in the two sub-populations.

The file `mydata.dat` contains two columns.  The first column is a set of samples from a distribution with variance 4, while the second column contains samples from a distribution with variance 16.  __Your task is to test whether the expectations of the two distributions that were sampled from are the same.__  To do this we proceed set the null and alternative hypotheses as follows:

![](https://render.githubusercontent.com/render/math?math=H_0:\mu_1-\mu_2=\theta_0\qquad\H_1:\mu_1-\mu_2\ne\theta_0)

Here ![](https://render.githubusercontent.com/render/math?math=\mu_1) and ![](https://render.githubusercontent.com/render/math?math=\mu_2) are the population means for the two distributions.  ![](https://render.githubusercontent.com/render/math?math=\theta_0) meanwhile is a constant that in this case is set equal to zero (I have introduced this constant to demonstrate that we can set the difference to any value).  We now introduce the following test statistic:

![](https://render.githubusercontent.com/render/math?math=T\frac{\frac{1}{n_1}\sum_{i=1}^{n_1}X_i-\frac{1}{n_2}\sum_{j=1}^{n_2}Y_j-\theta_0}{\sqrt{\frac{\sigma_1^2}{n_1}%2B\fraac{\sigma_2}{n_2}}})

The ![](https://render.githubusercontent.com/render/math?math=X_i) here are the ![](https://render.githubusercontent.com/render/math?math=n_1) samples that were obtained by sampling from the first distribution.  The first term in the numerator is thus a sample mean.  Similarly,  ![](https://render.githubusercontent.com/render/math?math=Y_j) in the second term is used to represent the ![](https://render.githubusercontent.com/render/math?math=n_2) samples that were obtained by sampling from the second distribution so this term is also a sample mean.  Under the assumption of the null hypothesis, the difference between the two sample means should be equal to ![](https://render.githubusercontent.com/render/math?math=theta_0).  The numerator of T is thus a sample from a distribution with an expectation of zero.

In the denominator, ![](https://render.githubusercontent.com/render/math?math=\sigma_1) is the standard deviation for the distribution from which the ![](https://render.githubusercontent.com/render/math?math=X_i) are sampled and ![](https://render.githubusercontent.com/render/math?math=\sigma_2) is the standard deviation for the distribution from which the ![](https://render.githubusercontent.com/render/math?math=Y_j) are sampled.  Squaring these two standard deviations and dividing them by ![](https://render.githubusercontent.com/render/math?math=n_1) and ![](https://render.githubusercontent.com/render/math?math=n_2) gives us the value of the variances for the distributions from which the two sample means are calculated by the central limit theorem.  In addition, we have also proved elsewhere that the variance for the difference between two random variables is the sum of the individual variances of the distribution.  The denominator is thus the standard deviation for the random variable that is computed in the numerator.  T is thus a sample from a standard normal random variable.

Having read the instructions above you should now be able to test whether or not the expectation of the distributions in the first and second columns of `mydata.dat` are the same or not.  To get you started I have written an outline of the functions that you need to write to complete the tests.  These functions are:

1. `testStatistic` - this function takes four arguments in input: a NumPy array called `data1` that contains the samples from the first distribution, a scalar called `sigma1` which is the standard deviation of the first distribution, a NumPy array called `data2` that contains the samples from the second distribution and a scalar called `sigma2` which is the standard deviation of the second distribution.  This function should return the test statistic, T, that is defined using the formula above.  
2. `pvalue` - this function takes four arguments in input: a NumPy array called `data1` that contains the samples from the first distribution, a scalar called `sigma1` which is the standard deviation of the first distribution, a NumPy array called `data2` that contains the samples from the second distribution and a scalar called `sigma2` which is the standard deviation of the second distribution.  Within this function the value of the `testStatistic` should be used to calculate the p-value.  The calculated p-value should then be returned. 
