import numpy as np
from scipy import stats
from scipy.stats import beta
import math
import matplotlib.pyplot as plt
n_control = 674
n_control_dead = 39
n_treatment = 680
n_treatment_dead = 22

alph = 1
bet = 1
prior = beta(alph, bet)
x = np.linspace(-0.001, .12, 1000)

contr_distr = beta(n_control_dead, n_control)
mean_c_distr = contr_distr.mean()
print(contr_distr)
print(mean_c_distr)
treat_distr = beta(n_treatment_dead, n_treatment)
mean_t_distr = treat_distr.mean()
print(treat_distr)
print(mean_t_distr)

pdf_c = contr_distr.pdf(x)
pdf_t = treat_distr.pdf(x)
odds = []

sample_cont = beta.rvs(n_control_dead, n_control, size=1000)
sample_treat = beta.rvs(n_treatment_dead, n_treatment, size=1000)

def odds_ratio(p0, p1):
   return ((p1/(1-p1))/(p0/(1-p0)))

for p0, p1 in zip(sample_cont, sample_treat):
    odds.append(odds_ratio(p0, p1))

pdf_prior = prior.pdf(x) 
# print(len(odds))

fig1, (ax1, ax2) = plt.subplots(2, 1)
ax1.hist(odds, np.arange(0, 2, 0.01))
ax2.plot(x, pdf_prior,label="Prior")
ax2.plot(x, pdf_c, label="control")
ax2.plot(x, pdf_t, label="treatment")
# decorate
ax1.set_title('Newcomb\'s measurements')
ax1.set_ylabel('count')
ax1.set_xlabel('odds ratio')
# ax2.set_xticks(np.arange(0,1.5,.1))


plt.show()