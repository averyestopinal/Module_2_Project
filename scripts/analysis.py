# Purpose:
#   This analysis script compares Sudoku solve times with vs without music using paired trials.
#   Primary test: one-sample t-test on matched (music - silence) differences.
#   Secondary check: paired t-test on participant means (descriptive).

import pandas as pd, numpy as np
from scipy import stats
import matplotlib.pyplot as plt, seaborn as sns
import os

df = pd.read_csv('data/cleaned/clean_data.csv')

# group data by condition variable and print summary stats
print("\n--- Descriptive statistics by condition ---")
print(df.groupby('condition')['time_sec'].describe())

# creating boxplot
plt.figure(figsize=(6,4))
sns.boxplot(x='condition', y='time_sec', data=df)
sns.stripplot(x='condition', y='time_sec', data=df, color='k', alpha=0.3, jitter=True)
plt.ylabel('Time (sec)')
plt.title('Sudoku solve time by condition')
plt.savefig('results/figures/boxplot_time.png', bbox_inches='tight')
plt.close()


# ------------------------------ CITED BLOCK ---------------------------------
# Used help of ChatGPT (OpenAI GPT-5, 11/2/2025 at ~8:10 pm) to implement this
# paired-difference analysis section. This code reshapes the data into matched pairs
# (same participant and puzzle) and runs a one-sample t-test on the differences
# (music − silence) to test our hypothesis that background music affects completion time.
# All experimental decisions, parameter choices, and interpretation are by the authors.

# pivot data so each row represents a matched pair: same participant + puzzle under both conditions
pivot = df.pivot_table(index=['participant','puzzle_id'],
                       columns='condition',
                       values='time_sec',
                       aggfunc='first').reset_index()

# remove incomplete pairs
pivot = pivot.dropna(subset=['music','silence']).copy()
pivot['diff'] = pivot['music'] - pivot['silence']   # positive -> slower with music

# descriptive stats for differences
n = len(pivot)
mean_diff = pivot['diff'].mean()
sd_diff = pivot['diff'].std(ddof=1)
se_diff = sd_diff / np.sqrt(n)
t_stat, p_val = stats.ttest_1samp(pivot['diff'], popmean=0)

# 95% CI for mean difference
t_crit = stats.t.ppf(1 - 0.025, df=n - 1)
ci_low = mean_diff - t_crit * se_diff
ci_high = mean_diff + t_crit * se_diff

# Cohen’s d (paired differences) to measure effect size across all matched pairs
cohen_d = mean_diff / sd_diff if sd_diff > 0 else np.nan

print("\n--- Paired (matched) difference analysis ---")
print(f"Number of pairs: {n}")
print(f"Mean difference (music - silence): {mean_diff:.2f} sec")
print(f"SD of differences: {sd_diff:.2f} sec")
print(f"95% CI: [{ci_low:.2f}, {ci_high:.2f}]")
print(f"One-sample t-test: t = {t_stat:.3f}, p = {p_val:.4f}")
print(f"Cohen's d (paired): {cohen_d:.3f}\n")

# save pair-level summary
os.makedirs('../results', exist_ok=True)
pivot[['participant','puzzle_id','music','silence','diff']].to_csv('results/summary_pairs.csv', index=False)

# -------------------------------- END OF CITED BLOCK --------------------------------

# calc each participant's avg time for each condition 
means = df.groupby(['participant','condition'])['time_sec'].mean().unstack()
means['diff'] = means['music'] - means['silence']
print(means)

# run paired t-test to compare each participant's mean (music vs silence)
if means.shape[0] >= 2:
    t,p = stats.ttest_rel(means['music'], means['silence'])
    print("paired t:", t, "p:", p)

# Cohen's d to see how big the diff is (measures effect size across participant means)
d = (means['diff'].mean()) / (means['diff'].std(ddof=1) if means['diff'].std(ddof=1)>0 else np.nan)
print("Cohen d (paired across participants):", d)

# save summary stats to a separate csv file
means.to_csv('results/summary_stats.csv')