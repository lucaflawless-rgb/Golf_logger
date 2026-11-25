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

A Python command line interface for managing, inspecting, inserting and visualizing golf round data using SQLite(`golf_data.db`), CSV source data(`Data_centric_programming.csv`) and `matpoltlib`.

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

### Files & description
| File | Description |
| :--- | :--- |
| `main.py` | Main Python CLI script for inspecting, inserting, and graphing golf data. |
| `Data_centric_programming.csv` | Source CSV file containing the initial golf records. |
| `golf_data.db` | SQLite database file storing the `scores` table. |
| `README.md` | Project documentation for the assignment. |



## References
- [Item 1](https://www.youtube.com/watch?v=vvKMxsee5uo)
- [Item 2](https://www.youtube.com/watch?v=-Wvt7lWxzf4)
- [Item 3](https://www.youtube.com/watch?v=D4VlmL3G4_o)

## What I am most proud of in the assignment
Im most proud of being able to put together a complete, working data aplication in Python that connects a CSV ingestion, A SQLite3 database `golf_data.db`, `pandas` filtering, and `matplotlib` visualizations inside a clean command-line menu. Also Graphing made the proect feel more practical and cohesive.

## What I learned
Completing this project helped me build practical skills working with `SQLite3`,`Pandas` and `matplotlib` within a commad line interface in python.I learned how to load CSV data into a SQLite database, query and filter records with `pandas`.I also gained a better understanding of handling user input errors, debugging menu flow and plotting behavior.

## Reflection 
Since completing this assignment I gave it few days to think about how i could have improved the overall design. One key issue I encountered was that I didn't have a way to edit or remove data from my  `SQLite` database, Which could lead to issues if the user wanted to change the date they inputted through the application.