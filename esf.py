from math import sqrt
import pandas as pd
from statsmodels.stats.proportion import proportion_effectsize
from statsmodels.stats.power import TTestIndPower

"""
Using Week 7 material to complete esf

A grade 2 bolt has a tensile strength of 74 kpsi, so this will be s_current
Since our non annealed bolts still cooled for a mean of 72 minutes, tensile strenth will likely be lower than 74 kpsi
"""

data = pd.read_csv('tensile_cooling_synthetic.csv')

M_grade2 = data.loc[data['group'] == 'short', 'tensile_strength_psi'].mean()
M_annealed =  data.loc[data['group'] == 'long', 'tensile_strength_psi'].mean()
# The above code snippet was generated using ChatGPT 5 on 11/2/25 at 11:45a and then modified in order to calcualte the std of the corrent columnM_annealed =  data.loc[data['group'] == 'long', 'tensile_strength_psi'].mean()

s = data.loc[data['group'] == 'long', 'tensile_strength_psi'].std()

# print(M_grade2)
# print(M_annealed)

# Defining tensile strength
s_annealed = 74000*.75
s_grade2 = 74000

# Standard values from lectures and slides
alpha = 0.05
power = 0.8

# Calculating Effect Size using Cohen's d
d = (M_grade2-M_annealed)/s
print(f'Effect size: {d}')

# Calculating Required Sample Size
obj = TTestIndPower()
n = obj.solve_power(effect_size=d, alpha=alpha, power=power, 
                    ratio=1, alternative='two-sided')

print(f'Sample size/Number needed in each group: {n}')

"""
Number needed in each group is 2.75 which is very low. For the robustness of the analysis, 50 should be safe to filter out any outliers
or unexpected data. An effect size of 3.38 is very large so it is easy to see the relationship between cooling time and tensile strength.
"""

