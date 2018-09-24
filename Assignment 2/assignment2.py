import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

data = open("algae.txt", "r")
data_as_list = data.read().split("\n")

#last row empty, excluded
del data_as_list[-1]

#n = number of observations
n = len(data_as_list)
#print(n)
#print(data_as_list[0], data_as_list[-1])
pos = float(data_as_list.count('1'))
neg = float(data_as_list.count('0'))
print(pos)
print(neg)

#count beta for prior and observations
pi_pri = beta(2,10)
pi_obs = beta(pos +2, neg + 10)

mean_pri = pi_pri.mean()
mean_obs = pi_obs.mean()
diff_mean = mean_pri/mean_obs
print(mean_pri)
print(mean_obs)
print((diff_mean-1)*100,"%")

range_bet = np.arange(0, 1, 0.001)
pdf_pri = pi_pri.pdf(range_bet)
pdf_obs = pi_obs.pdf(range_bet)

#b. with cdf
pi0 = pi_obs.cdf(0.2)
prob_pi0 = pi0 * 100
print("b:", prob_pi0, "%")


f, ax = plt.subplots()
ax.set_title("Beta(Prior) and Beta(Obs)")
ax.plot(range_bet, pdf_pri)
ax.plot(range_bet, pdf_obs)
plt.show()
