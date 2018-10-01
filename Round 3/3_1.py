import numpy as np
from scipy import stats
from scipy.stats import beta, t
import math

import matplotlib.pyplot as plt

import sinvchi2
import plot_tools
data = open("windshieldy1.txt", "r")
data_as_list = data.read().split("\n")
del data_as_list[-1]
data_as_float = []
for item in data_as_list:
    data_as_float.append(float(item))
#avg = np.average(data_as_float)

n = len(data_as_float)
print(data_as_float)
print("n", n)
print(data_as_float)
s2 = np.var(data_as_float, ddof=1)

my = np.mean(data_as_float)
print(s2)
print(my)

tl1 = [10, 20]

t1 = np.linspace(tl1[0], tl1[1], 100)

# compute the exact marginal density for mu
# multiplication by 1./sqrt(s2/n) is due to the transformation of variable
# z=(x-mean(y))/sqrt(s2/n), see BDA3 p. 21
pm_mu = stats.t.pdf((t1 - my) / np.sqrt(s2/n), n-1) / np.sqrt(s2/n)

# compute the exact marginal density for mu for the filtered data

# Plotting
# create figure
fig, axes = plt.subplots(2, 1, sharex=True, figsize=(8, 8))

# plot histogram
ax = axes[0]
ax.hist(data_as_float, np.arange(10, 20, 2))
# decorate
ax.set_title(' ')
ax.set_ylabel('count')
ax.set_xlabel('$\mu$')
plt.setp(axes[0].get_xticklabels(), visible=True)

z_critical = stats.norm.ppf(q = 0.95)  # Get the z-critical value*

print("z-critical value:")              # Check the z-critical value
print(z_critical)                        

pop_stdev = 1  # Get the population standard deviation

margin_of_error = z_critical * (pop_stdev/math.sqrt(2))

confidence_interval = (my - margin_of_error,
                       my + margin_of_error)  

print("Confidence interval:")
print(confidence_interval)
print("t: ",t.ppf(1 - 0.5, df=9))
# plot the posterior of mu
ax = axes[1]
ax.plot(t1, pm_mu)
t1_95_idx1 = (t1 > confidence_interval[0]) & (t1 < confidence_interval[1])
plt.fill_between(t1[t1_95_idx1], pm_mu[t1_95_idx1], color='0.90')
# Plot the currently accepted true value
ax.axvline(my, color='k', linestyle='--')
ax.legend(
    ('posterior of $\mu$',
     'posterior of $\mu$ given $y > 0$ : %.2f' %my ,
     '"Confidence"'),
    loc='upper left'
)
ax.set_title('Normal model')
ax.set_xlabel('$\mu$')
ax.set_yticks(np.arange(0,1.1,0.1))
ax.set_xticks(np.arange(12,18,2))
# set bottom to zero
ax.set_ylim((0, ax.set_ylim()[1]))

fig.tight_layout()
plt.show()
