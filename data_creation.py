import pandas as pd

"""
Bolt annealing will be used as the parallel for data creation. Information on bolt annealing
can be found here: https://www.instructables.com/An-Introduction-to-Heat-Treating-Carbon-Steels-Ann/.

This states cooling should be cooled no faster than 70 degrees per hour between critical temp and 
(critical temp - 100 degrees fareneheit). Therefore, proper cooling time will be > 86 minutes. There
will be 2 groups: long and short cooling times. Long cooling time mean will be 100 minutes. SHort cooling
time mean will be 72 minutes. This is so both are a standard diavation of 14 from minimum proper cooling 
time.
"""

# --- Synthetic Data Generator: Tensile Strength vs Cooling Time ---
# Short cooling: ~74 ksi mean
# Long cooling: lower mean (~60–65 ksi, over-annealed)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

# Sample sizes
n_per_group = 150

# Cooling time distributions
cooling_long = np.random.normal(loc=100, scale=4, size=n_per_group)
cooling_short = np.random.normal(loc=72, scale=4, size=n_per_group)

# Model parameters
peak_strength = 76000.0        # psi, peak at proper 86 min
b_short_side = 15.0            # penalty coefficient for short (<86)
b_long_side  = 35.0            # stronger penalty for long (>86)
long_group_offset = -9000.0    # additional downward offset for long cooling
noise_sd = 800.0               # random noise in psi

def tensile_from_time(t):
    """Piecewise quadratic model with different slopes on each side of 86 min."""
    b = np.where(t < 86, b_short_side, b_long_side)
    return peak_strength - b * (t - 86)**2

# Generate tensile strengths
tensile_short = tensile_from_time(cooling_short) + np.random.normal(0, noise_sd, n_per_group)
tensile_long  = tensile_from_time(cooling_long)  + np.random.normal(0, noise_sd, n_per_group) + long_group_offset

# Combine into dataframe
df_short = pd.DataFrame({
    "group": "short",
    "cooling_time_min": cooling_short,
    "tensile_strength_psi": tensile_short
})

df_long = pd.DataFrame({
    "group": "long",
    "cooling_time_min": cooling_long,
    "tensile_strength_psi": tensile_long
})

df = pd.concat([df_short, df_long], ignore_index=True)
df["tensile_strength_psi"] = df["tensile_strength_psi"].clip(lower=0.0)

# Save
df.to_csv("tensile_cooling_synthetic.csv", index=False)



# https://chatgpt.com/share/e/69078466-7d30-8006-aeb4-5990e01ec235

