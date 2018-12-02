#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import scipy
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[12]:


pop1 = np.random.binomial(10, 0.2, 10000)
pop2 = np.random.binomial(10,0.5, 10000)

sample1 = np.random.choice(pop1, 100, replace=True)
sample2 = np.random.choice(pop2, 100, replace=True)

mean1 = sample1.mean()
mean2 = sample2.mean()

std1 = sample1.std()
std2 = sample2.std()

print('Mean 1 =', mean1)
print('Mean 2 =', mean2)
print('Standard Deviation 1 =',std1)
print('Standard Deviation 1 =',std2)

plt.hist(sample1, alpha=0.5, label='sample 1') 
plt.hist(sample2, alpha=0.5, label='sample 2') 
plt.legend(loc='upper right') 

plt.axvline(sample1.mean(), color='b', linestyle='solid', linewidth=2)
plt.axvline(sample1.mean() + sample1.std(), color='b', linestyle='dashed', linewidth=2)
plt.axvline(sample1.mean()-sample1.std(), color='b', linestyle='dashed', linewidth=2) 

plt.axvline(sample2.mean(), color='r', linestyle='solid', linewidth=2)
plt.axvline(sample2.mean() + sample2.std(), color='r', linestyle='dashed', linewidth=2)
plt.axvline(sample2.mean()-sample2.std(), color='r', linestyle='dashed', linewidth=2) 

plt.show()


# In[14]:


##The histograms should appear similar as well as the means and standard deviations.
##The test is performed the same number of times but the sample is 10 times larger which should make the bins 10 times
## taller but still distributed similarly since the probability of success is still 0.2 and 0.5

sample3 = np.random.choice(pop1, 1000, replace=True)
sample4 = np.random.choice(pop2, 1000, replace=True)

mean3 = sample3.mean()
mean4 = sample4.mean()

std3 = sample3.std()
std4 = sample4.std()

print('Mean 1 =', mean3)
print('Mean 2 =', mean4)
print('Standard Deviation 1 =',std3)
print('Standard Deviation 1 =',std4)

plt.hist(sample3, alpha=0.5, label='sample 1') 
plt.hist(sample4, alpha=0.5, label='sample 2') 
plt.legend(loc='upper right') 

plt.axvline(sample3.mean(), color='b', linestyle='solid', linewidth=2)
plt.axvline(sample3.mean() + sample1.std(), color='b', linestyle='dashed', linewidth=2)
plt.axvline(sample3.mean()-sample1.std(), color='b', linestyle='dashed', linewidth=2) 

plt.axvline(sample4.mean(), color='r', linestyle='solid', linewidth=2)
plt.axvline(sample4.mean() + sample2.std(), color='r', linestyle='dashed', linewidth=2)
plt.axvline(sample4.mean()-sample2.std(), color='r', linestyle='dashed', linewidth=2) 

plt.show()

##The histograms are different which could be accounted for through the smaller sample size changing the distribution.
##It would be expected that as the sample sizes became larger and larger that the histograms and distribustions would look
##more and more alike as there would be more samples to even out the distribution.
##The means and standard deviations are still close as expected since each test is still the same 10 repetions and the
##probability of success is still the same


# In[17]:


##I would expect the histograms to look less similar as the sample size is significantly smaller and would be more likely
## to be more unevenly distrubted as there are less items to even out the averages. I would also think that the means and 
## standard deviations would be more unpredictable and to be less likely to be centered nicely as the other two plots have.

sample5 = np.random.choice(pop1, 20, replace=True)
sample6 = np.random.choice(pop2, 20, replace=True)

mean5 = sample3.mean()
mean6 = sample4.mean()

std5 = sample5.std()
std6 = sample6.std()

print('Mean 1 =', mean5)
print('Mean 2 =', mean6)
print('Standard Deviation 1 =',std5)
print('Standard Deviation 1 =',std6)

plt.hist(sample5, alpha=0.5, label='sample 1') 
plt.hist(sample6, alpha=0.5, label='sample 2') 
plt.legend(loc='upper right') 

plt.axvline(sample5.mean(), color='b', linestyle='solid', linewidth=2)
plt.axvline(sample5.mean() + sample1.std(), color='b', linestyle='dashed', linewidth=2)
plt.axvline(sample5.mean()-sample1.std(), color='b', linestyle='dashed', linewidth=2) 

plt.axvline(sample6.mean(), color='r', linestyle='solid', linewidth=2)
plt.axvline(sample6.mean() + sample2.std(), color='r', linestyle='dashed', linewidth=2)
plt.axvline(sample6.mean()-sample2.std(), color='r', linestyle='dashed', linewidth=2) 

plt.show()

## The plots show more difference because of the smaller sample size, however the means and standard deviations are still
## close in value which could be attributed to the fact that the numbers only range from 0-10 which doesn't give a 
## large area for different numbers to occur such as if the values could be 0-10000


# In[25]:


##I would expect the plot for sample1 to shift to the right with a higher concentration on the higher numbers but not far
## enough to overlap sample2 significantly. This would happen because the probability of success in pop1 has risen but
## not as high as the probability of success for pop2
##I would also think that the mean would be higher for sample1 as the number of success should have gone up, but the 
##standard deviation should have remained around the same since the experiament is still performed in the same way with 
##the same popluation, number of repetitions for each iteration and number of iterations
##The t-value should be relatively high and the p-value should be relatively low as the samples are not very similar.
##The t-value shows how similar the two samples are and the p-value shows the likelihood of differences due to sampling 
##errors which would be unlikely since the difference would be more likely to be attributed to the actual differences 
##in the samples

pop1 = np.random.binomial(10, 0.3, 10000)
pop2 = np.random.binomial(10,0.5, 10000)

sample1 = np.random.choice(pop1, 100, replace=True)
sample2 = np.random.choice(pop2, 100, replace=True)

mean1 = sample1.mean()
mean2 = sample2.mean()

std1 = sample1.std()
std2 = sample2.std()


print('Mean 1 =', mean1)
print('Mean 2 =', mean2)
print('Standard Deviation 1 =',std1)
print('Standard Deviation 1 =',std2)

print(ttest_ind(sample2, sample1, equal_var=False))

plt.hist(sample1, alpha=0.5, label='sample 1') 
plt.hist(sample2, alpha=0.5, label='sample 2') 
plt.legend(loc='upper right') 

plt.axvline(sample1.mean(), color='b', linestyle='solid', linewidth=2)
plt.axvline(sample1.mean() + sample1.std(), color='b', linestyle='dashed', linewidth=2)
plt.axvline(sample1.mean()-sample1.std(), color='b', linestyle='dashed', linewidth=2) 

plt.axvline(sample2.mean(), color='r', linestyle='solid', linewidth=2)
plt.axvline(sample2.mean() + sample2.std(), color='r', linestyle='dashed', linewidth=2)
plt.axvline(sample2.mean()-sample2.std(), color='r', linestyle='dashed', linewidth=2) 

plt.show()

##The plot for sample1 has shifted to the right into the higher values but does not overlap sample2 and the mean has 
##increased for sample1 for the reasons stated above. The standard deviation for sample1 is still about the same
##P-value is relatively low but not extremely, likely because the sample size is only 1% of the population
##T-value is high for the reason stated above


# In[26]:


##I would expect the plot for sample1 to shift even further into the higher numbers and shift further to the right as the
##probability for success is higher now. It should come closer to the plot of sample2 but not overlap it entirely as the 
## probaility of success is still lower for sample1 than sample2
##The mean should be higher than the original and last example and the standard deviation should remain around the same
##t-value should be lower because as the samples become more similar in probability the t-value reflects this.
##the p-value should be higher because as the populations get more similar any differences should be attributed to sampling
##error and not actual differences

pop1 = np.random.binomial(10, 0.4, 10000)
pop2 = np.random.binomial(10,0.5, 10000)

sample1 = np.random.choice(pop1, 100, replace=True)
sample2 = np.random.choice(pop2, 100, replace=True)

mean1 = sample1.mean()
mean2 = sample2.mean()

std1 = sample1.std()
std2 = sample2.std()

print('Mean 1 =', mean1)
print('Mean 2 =', mean2)
print('Standard Deviation 1 =',std1)
print('Standard Deviation 1 =',std2)

print(ttest_ind(sample2, sample1, equal_var=False))

plt.hist(sample1, alpha=0.5, label='sample 1') 
plt.hist(sample2, alpha=0.5, label='sample 2') 
plt.legend(loc='upper right') 

plt.axvline(sample1.mean(), color='b', linestyle='solid', linewidth=2)
plt.axvline(sample1.mean() + sample1.std(), color='b', linestyle='dashed', linewidth=2)
plt.axvline(sample1.mean()-sample1.std(), color='b', linestyle='dashed', linewidth=2) 

plt.axvline(sample2.mean(), color='r', linestyle='solid', linewidth=2)
plt.axvline(sample2.mean() + sample2.std(), color='r', linestyle='dashed', linewidth=2)
plt.axvline(sample2.mean()-sample2.std(), color='r', linestyle='dashed', linewidth=2) 

plt.show()

##Predications for the plots, means,standard deviations, t-value and p-value were correct for the reasons stated above


# In[ ]:





# In[7]:


##The orginal histogram of sample of binomial(10,0.2,10000) and binomia(10,0.5,10000) should look very different from the 
##current distribuation of the negative binomial with the same parameters. The binomial is predicting the likelihood of a 
##certain number of success given only 2 outcomes, while the negative binomial is predicting the probability of the number
##of times the experiament needs to be repeated before the first success. This should cause the plots to look different.
##Sample2 should be further to the left with smaller number more frequently as the probility of success being 0.5 makes
##it mor likely that there will be less tests until success is achieved and sample1 should be further to the left with more
## frequeent larger numbers as the probability of success is lower and more tests should be required to produce a success

pop1 = np.random.negative_binomial(10, 0.2, 10000)
pop2 = np.random.negative_binomial(10,0.5, 10000)

sample1 = np.random.choice(pop1, 100, replace=True)
sample2 = np.random.choice(pop2, 100, replace=True)

mean1 = sample1.mean()
mean2 = sample2.mean()

std1 = sample1.std()
std2 = sample2.std()


print(mean1)
print(mean2)
print(std1)
print(std2)

plt.hist(sample1, alpha=0.5, label='sample 1') 
plt.hist(sample2, alpha=0.5, label='sample 2') 
plt.legend(loc='upper right') 

plt.axvline(sample1.mean(), color='b', linestyle='solid', linewidth=2)
plt.axvline(sample1.mean() + sample1.std(), color='b', linestyle='dashed', linewidth=2)
plt.axvline(sample1.mean()-sample1.std(), color='b', linestyle='dashed', linewidth=2) 

plt.axvline(sample2.mean(), color='r', linestyle='solid', linewidth=2)
plt.axvline(sample2.mean() + sample2.std(), color='r', linestyle='dashed', linewidth=2)
plt.axvline(sample2.mean()-sample2.std(), color='r', linestyle='dashed', linewidth=2) 

plt.show()

##All predications were correct for reasons stated above


# In[ ]:




