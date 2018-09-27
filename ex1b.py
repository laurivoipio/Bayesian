import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt
my = 0.2
sig2 = 0.01

alph = ((my*((my*(1-my)/sig2)-1)))

bet = (((alph*(1-my)/my)))
#print(alph)
#print(bet)
a, b = -0.5, 1.2
range = np.linspace(a, b, 50000)
#print(range)

ss = beta.pdf(range, alph, bet)
#print(ss)

#graph
f, ax = plt.subplots()
ax.plot(range, ss, label='pdf')
ax.set_title('Beta distribution')

#histogram
r = beta.rvs(alph, bet, size=1000)
#print(r)
ax.hist(r, normed=True, histtype='step', alpha=alph, label='history')
ax.legend(loc='best', frameon=False)

plt.show()

