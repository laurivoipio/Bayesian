import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt
my = 0.2
sig2 = 0.01

alph = ((my*((my*(1-my)/sig2)-1)))

bet = (((alph*(1-my)/my)))
#print(alph)
#print(bet)
range = np.linspace(-0.5,1.2,50000)
#print(range)

ss = beta.pdf(range, alph, bet)
#print(ss)

f, ax = plt.subplots()
ax.plot(range, ss)
ax.set_title('Beta distribution')
plt.show()
