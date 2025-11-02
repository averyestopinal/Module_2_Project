from math import sqrt
from statsmodels.stats.proportion import proportion_effectsize
from statsmodels.stats.power import TTestIndPower

"""
Using Week 7 material to complete esf

"""

# Defining probabilities
p_new = 
p_current = 

# Standard values from lectures and slides
alpha = 0.05
power = 0.8

# Calculating Effect Size
d = proportion_effectsize(p_new, p_current, method='normal')
print(f'Effect size: {d}')

# Calculating Required Sample Size
obj = TTestIndPower()
n = obj.solve_power(effect_size=d, alpha=alpha, power=power, 
                    ratio=1, alternative='two-sided')

print('Sample size/Number needed in each group: {:.3f}'.format(n))