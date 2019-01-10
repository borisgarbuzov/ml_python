import numpy as np

def dependent(mu = 1, sigma = 2, size = 1000, n = 10):
    sample = np.random.normal(mu, sigma, size)
    sum_of_samples = 0
    var_lst = [0,]
    for i in range(n):
        sum_of_samples += sample
        var_lst.append(np.var(sum_of_samples))
    return var_lst


def independent(mu = 1, sigma = 2, size = 1000, n = 10):
    sample_1 = np.random.normal(mu, sigma, size)
    sum_of_samples = sample_1
    var_lst = [0, np.var(sum_of_samples)]
    for i in range(n-1):
        sample_n = np.random.normal(mu, sigma, size)
        sum_of_samples += sample_n
        var_lst.append(np.var(sum_of_samples))
    return var_lst



import matplotlib.pyplot as plt

dep = dependent()
indep = independent()
plt.plot(dep, '--')
plt.plot(indep, '-')
plt.legend(['dependent', 'independent'], loc='upper left')
plt.show()

LRVdep = [itm/idx for idx, itm in enumerate(dep) if idx > 0]
LRVindep = [itm/idx for idx, itm in enumerate(indep) if idx > 0]
plt.plot(LRVdep, '--')
plt.plot(LRVindep, '-')
plt.legend(['LRv dependent', 'LRV independent'], loc='upper left')
plt.show()
