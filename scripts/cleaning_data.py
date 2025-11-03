import pandas as pd

raw = pd.read_csv('data/raw/Sudoku trials  - trials.csv')
cleaned = raw.copy()

# Data Structure and Quality
print("Data Structure")
print("---------------")
print(f"Dimensions: {cleaned.shape}")
print(f"Data Types:\n{cleaned.dtypes}")
print(f"Missing Values:\n{cleaned.isnull().sum()}")


# There are randomly capitalized rows in particpant and condition, lower case all entries and remove white space
cleaned["participant"] = cleaned["participant"].str.lower().str.strip()
cleaned["condition"] = cleaned["condition"].str.lower().str.strip()

"""
There are empty rows in correct
If there is a time for completion, but correct is not marked 1.0 fill with 1.o, then convert to int
"""
cleaned.loc[cleaned['time_sec'].notnull() & cleaned['correct'].isnull(), 'correct'] = 1
cleaned['correct'] = cleaned['correct'].astype(int)
# The above code snippet was generated using ChatGPT5 on 11/2/25 at 8:45p and midified to correctly identify columns.

# Saving data
cleaned.to_csv('data/cleaned/clean_data.csv', index=False)