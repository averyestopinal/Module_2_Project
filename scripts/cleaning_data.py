import pandas as pd

raw = pd.read_csv('data/raw/Sudoku trials  - trials.csv')
cleaned = raw

# Data Structure
print("Data Structure")
print("---------------")
print(f"Dimensions: {raw.shape}")
print(f"Data Types:\n{raw.dtypes}")
print(f"Missing Values:\n{raw.isnull().sum()}")

# Data Quality
print("\nData Quality")
print("------------")
print(f"Duplicated Rows: {raw.duplicated().sum()}")
print("Checking for Inconsistent Values:")
print(raw.apply(lambda x: x.value_counts().index[0]).to_frame('most_frequent_value'))

# Looking at data
# print(raw)

# There are randomly capitalized rows in particpant and condition, lower case all entries
cleaned["participant"] = cleaned["participant"].str.lower()
cleaned["condition"] = cleaned["condition"].str.lower()

"""
There are empty rows in correct
If there is a time for completion, but correct is not marked 1.0 fill with 1.0
"""
cleaned.loc[cleaned['time_sec'].notnull() & cleaned['correct'].isnull(), 'correct'] = 1.0
# The above code snippet was generated using ChatGPT5 on 11/2/25 at 8:45p and midified to correctly identify columns.

# Saving data
cleaned.to_csv('data/cleaned/cleaned_trails.csv', index=False)