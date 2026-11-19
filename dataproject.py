import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os 

DB_NAME = "golf_data.db"
CSV_PATH = "Data_centric_programming.csv"  

def initialize_database():
    conn = sqlite3.connect(DB_NAME)
    if os.path.exists(CSV_PATH):
        df = pd.read_csv(CSV_PATH)
        df.columns = df.columns.str.strip()
        df.to_sql('scores', conn, if_exists='replace', index=False)
    conn.close()


def main():
    initialize_database()
    select = 0

    while select != 4:
        print('\n====Main menu=====')
        print('\n Select an option')
        print ('\n\n 1.Inspect Data')
        print('\n\n 2.Insert Data')
        print('\n\n 3.Graph Data')
        print('\n\n 4.Quit')
        print('\n+++++++++++++++++++')
    
        try:
            select = int(input("choose an option: "))
        except ValueError:
            print("Please enter a valid number")
            continue
  
  
        if (select == 1):
            conn = sqlite3.connect(DB_NAME)
            df = pd.read_sql("SELECT * FROM scores", conn)
            conn.close()
            print("\n-----DATA INSPECTION-----")
            print("1. View all the data")
            print("2. Filter Data by date")
            
            
            try:
                option = int(input("Choose option (1 or 2): "))
            except ValueError:
                print("Please enter a valid number.")
                
            if option == 2:
                print("\nAvailable dates in dataset:")
                print(df['Date'].unique())
            
                user_date = input("Enter a date you wish to see (DD/MM/YYYY): ").strip()
                filtered_df = df[df['Date'] == user_date]
            
                if filtered_df.empty:
                    print(f"\n[!] No records found for date {user_date}")
                else:
                    print(f"\n--- Records for {user_date} ---")
                    print(filtered_df)
                    print(f"Number of rows found: {len(filtered_df)}")
                    
            elif option == 1:
                print("\n-----ALL DATA-----")
                print(df)
                print(f"Number of rows: {len(df)}")
                print("Average Score:", df['score'].mean())
            
            else:
                print(option, "is an invalid option you will return to the main menu")
                
            
                
            
                
        elif(select == 2):
            print("\n[Option 2 selected - insert new data]")
            print("\n -----INSERT NEW DATA-----")
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            
            Num = cursor.execute('SELECT COUNT(*) FROM scores').fetchone()[0] + 1
            Name = input("Name: ")
            Score = int(input("Score: "))
            Par = int(input("Par: "))
            Over_Par = int(Score) - int(Par)
            Wind = input("Wind Speed: ").strip()
            Date = input("Date: ")
            
            RowId = f"ID {Num}"
            Wind_Speed = f"{Wind}km/h"              
            
            cursor.execute('insert into scores ("Row ID", Name, score, par, "Over par", "Wind Speed", Date) values(?,?,?,?,?,?,?)', 
            (RowId,Name,Score,Par,Over_Par,Wind_Speed,Date))
            
            conn.commit() 
            conn.close()
            
            print(f"Added {RowId} for {Name} ({Over_Par} to par).")
            
        elif(select == 3):
            print("\n[Option 3 selected - Work in progress")

        elif(select == 4):
            print("\nGoodbye!")

        else:
            print("You have selected an invalid option")

if __name__ == "__main__":
    main()