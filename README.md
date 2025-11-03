# Module 2 Project
This project tests whether background music affects solving puzzle challenges such as Sudoku. Two participles each completed 20 puzzles (10 with music, 10 in silence), producing 40 trial-level observations per condition. We analyzed the data using paired t-tests and confidence intervals to determine is background music has a significant effect.

This project contains data cleaning and analysis for questioning if music significantly affects the
completion time of a Sudoku puzzle. This is a valuable analoge for studying the effects of music
on work efficiency.

## Structure
Module_2_Project/
├── data/
│ ├── raw/ # Original raw data
│ └── cleaned/ # Cleaned data
├── puzzles/ # Puzzle png files
├── results/ # Output from analysis
│ ├── figures/ #Output figures
├── scripts/ # Python scripts for cleaning and analysis
└── README.md

## Directions for Reproduction:
```bash 
git clone https://github.com/averyestopinal/Module_2_Project.git
cd Module_2_Project
python scripts/cleaning_data.py
python scripts/analysis.py

