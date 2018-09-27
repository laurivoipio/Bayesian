import numpy as np
from scipy.stats import beta
from scipy.stats import sem
from scipy.stats import t
from statsmodels.stats.weightstats.DescrStats.t import conflict_mean
import matplotlib.pyplot as plt
my = 0.2
sig2 = 0.01

alph = ((my*((my*(1-my)/sig2)-1)))

bet = (((alph*(1-my)/my)))

a, b = -0.5, 1.2
range = np.linspace(a, b, 50000)


ss = beta.pdf(range, alph, bet)


# a. graph
f, ax = plt.subplots()
ax.plot(range, ss, label='pdf')
ax.set_title('Beta distribution')

# b. histogram
r = beta.rvs(alph, bet, size=1000)
ax.hist(r, normed=True, histtype='step', alpha=alph, label='history')
ax.legend(loc='best', frameon=False)

# c. mean
me = np.mean(r)
diff_me = ((me/my)-1)*100
print("mean      ", me)
print("difference", diff_me, "%")
print()

# c. variance
va = np.var(r)
diff_va = ((va/sig2)-1)*100
print("variance  ", va)
print("difference", diff_va, "%")
print()

# d. percentile
perc = np.percentile(r, 95)
print ("percentile", perc)

