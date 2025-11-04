
# Module 2 Project
## Effect of Background Music on Sudoku Solving Time
This project tests whether background music affects solving puzzle challenges such as Sudoku. Two participles each completed 20 puzzles (10 with music, 10 in silence), producing 40 trial-level observations per condition. We analyzed the data using paired t-tests and confidence intervals to determine is background music has a significant effect.

This project contains data cleaning and analysis for questioning if music significantly affects the
completion time of a Sudoku puzzle. This is a valuable analoge for studying the effects of music
on work efficiency.

## Research Question
Does background music influence how quickly a person can complete a Sudoku puzzle?

### Hypotheses
- **H₀ (Null):** Background music has no effect on Sudoku puzzle completion time or accuracy.  
- **H₁ (Alternative):** Background music significantly affects Sudoku puzzle completion time or accuracy.
- 
## Structure
```
Module_2_Project/
├── data/
│ ├── raw/ # Original raw data
│ └── cleaned/ # Cleaned data
├── puzzles/ # Puzzle png files
├── results/ # Output from analysis
│ ├── figures/ #Output figures
├── scripts/ # Python scripts for cleaning and analysis
└── README.md
```

## Directions for Reproduction:
Clone the repository and run the cleaning and analysis scripts sequentially:

```bash 
git clone https://github.com/averyestopinal/Module_2_Project.git
cd Module_2_Project
python scripts/cleaning_data.py
python scripts/analysis.py
```

## Dependencies
Install dependencied by running ``` pip install -r requirements.txt ```

## Summary of Results
https://bylinedocs.com/document/354e3df1-1cfb-4f1c-9912-624a0334c604

## Presentation 
https://www.canva.com/design/DAG3rOHoClg/tEzS9i3AzSaXj9XPJ0RoFg/view?utm_content=DAG3rOHoClg&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=hfe7526762c 

## Collaborators
Avery Estopinal & Eugenia Tate: both authors contributed equally to experiment design, data collection, analysis, and writing.

## References
Used the help of ChatGPT (OpenAI GPT-5, 11/2–11/3/2025) for 2 cited code snippets within cleaning_data.py and analysis.py scripts in order to: 
- typecast double to int within cleaning_data.py
- implement complex paired-difference analysis section within analysis.py
