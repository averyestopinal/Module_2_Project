"""
Since the data is unpaired, normally distributed, and of around equal variance an unpaired t-test in right here
An unpiared t-test is governed by t = (X1-X2)/sqrt[(s1^2/n1)+(s2^2/n2)]
If t > t_critical from t-distrubution table, reject H0
"""

import numpy as np
import pandas as pd

data = pd.read_csv('tensile_cooling_synthetic.csv')

M_grade2 = data.loc[data['group'] == 'short', 'tensile_strength_psi'].mean()
M_annealed = data.loc[data['group'] == 'long', 'tensile_strength_psi'].mean()

s_grade2 = data.loc[data['group'] == 'short', 'tensile_strength_psi'].std()
s_annealed = data.loc[data['group'] == 'long', 'tensile_strength_psi'].std()

t = (M_annealed-M_grade2)/np.sqrt((s_annealed*s_annealed)/150+(s_grade2*s_grade2)/150)
print(f't score: {t}')

