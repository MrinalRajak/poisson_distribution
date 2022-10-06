
# Poisson Distribution


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
import seaborn as sb
data_poisson=poisson.rvs(mu=4,size=10000)
ax=sb.distplot(data_poisson,kde=True,color='green',hist_kws={"linewidth":25,'alpha':1})
ax.set(xlabel="Value",ylabel="Frequency")
plt.title("Poisson Distribution")
plt.show()
