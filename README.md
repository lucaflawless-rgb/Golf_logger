# Data Centric Programming Assignment 2026

- Golf Round Logger & Visualizer


## Data Dictionary
* Column Name - Data Type - Description.
* 'Rod ID' - TEXT - Unique identifer for each row (e.g Primary Key in Dataset).
* 'Name' -  TEXT - Player Name.
* 'Score' - INTEGER - Total amount of strokes across full round.
* 'Par' - INTEGER - Par value of the course.
* 'Over par' - INTEGER - Calculated difference between 'Score' and 'Par'.
* 'Wind Speed' - TEXT - Recorded wind speed (e.g 19KM/H).
* 'Date' - TEXT - Date of round ('DD/MM/YYYY')

## Description of the project

A Python command line interface for managing, inspecting, inserting and visualizing golf round data using SQLite('golf_data.db'), CSV source data('Data_centric_programming.csv') and 'matpoltlib'.

## Instructions for use

### 1. Required setup 
Ensure python is download alongside required libaries 'Pandas' and 'matplotlib'

### 2.Project Setup
Place the following files in the same project direactory
* main.py
* Data_centric_programming.csv

### Navigating the Main Menu
1. Inspect Data
    * Press 1 to display all data 
    * Press 2 this allows you to filter data by date
2. Insert Data
    * Follow prompts to enter Name, Score, Par, Wind speed and Date
    * Application automatically calculates Over par and Row Id
3.  Graph Data
    * Press 1 to plot Over par for all entries as a line graph 
    * Press 2 to plot Average Score by player as a bar chart
4.  Quit 
    * Press 4 to exit application
## How it works:
- **Database Setup:** Loads `Data_centric_programming.csv` via `pandas` into the `scores` table in `golf_data.db` (`sqlite3`).
- **Menu & Input:** Loops through options `1`–`4` with basic input validation until `4` is chosen.
- **Inspect (Option 1):** Views all rows (plus average score) or filters entries by `Date`.
- **Insert (Option 2):** Auto-assigns the next `Row ID`, calculates `Over par` (`score - par`), formats `Wind Speed`, and saves to SQLite.
- **Graph (Option 3):** Uses `pandas` and `matplotlib` to chart `Over par` across entries or average `score` by player.
## Findings


## List of files in the project

### Files & Source
| Files | Source |
| :--- | :--- |
| `main.py` | Self written |
| `test.py` | Self written |
| `test.py`


## References
- Item 1
- Item 2

## What I am most proud of in the assignment
Bla bla bla

## What I learned
Bla bla bla