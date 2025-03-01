import os
import csv

from dataHandler import (
    insertRecord,
    findRecords,
    loadInfoDat  
)
from hashFunction import customHash
from puntPlay import PuntPlay

def main():
    dataDirectory = os.path.join("data", "segundaprogramada")
    
    loadInfoDat(dataDirectory)

    while True:
        print("\n=== MAIN MENU ===")
        print("1. Load data from CSV (from firstTask's results)")
        print("2. Search data by hash position (0..749)")
        print("3. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            loadCsvData(dataDirectory)
        elif choice == "2":
            searchData(dataDirectory)
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid option. Please try again.")

def loadCsvData(dataDirectory):
    """
    Reads CSV files from the 'data/primeraprogramada/results' folder,
    creates PuntPlay objects, calculates their hash position, 
    and inserts them into info.dat.
    """

    currentDir = os.path.dirname(os.path.abspath(__file__))
    csvDir = os.path.join(currentDir, "..", "primeraprogramada", "results")


    csvFiles = [
        "part1-bubble-result.csv",
        "part1-insertion-result.csv",
        "part1-merge_sort-result.csv",
        "part1-quicksort-result.csv",
        # "part2-bubble-result.csv",
        # "part2-insertion-result.csv",
        # "part2-merge_sort-result.csv",
        # "part2-quicksort-result.csv",
    ]
    
    for csvFile in csvFiles:
        csvPath = os.path.join(csvDir, csvFile)
        if not os.path.exists(csvPath):
            print(f"File not found: {csvPath}. Skipping.")
            continue
        
        with open(csvPath, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)  
            
            for row in reader:
                gameId = row[0]
                teams = row[1]
                yards = row[2]
                qtr = row[3]
                dateStr = None  
                timeStr = None

                puntObj = PuntPlay(gameId, teams, yards, qtr, dateStr, timeStr)
                
                homeTeam = getHomeTeam(teams)
                
                position = customHash(puntObj.date, puntObj.qtr, homeTeam)
                
                insertRecord(dataDirectory, position, puntObj)
    
    print("Loading data completed.")

def getHomeTeam(teamsStr):
    """
    Example function to split 'AwayTeam@HomeTeam' and return the home team part.
    Adjust the logic as needed for your data format.
    """
    if "@" in teamsStr:
        parts = teamsStr.split("@")
        if len(parts) == 2:
            return parts[1]
    return teamsStr  

def searchData(dataDirectory):
    """
    Prompts user for a position [0..749], then fetches any record(s) at that position 
    (including collisions) and displays them.
    """
    try:
        key = int(input("Enter a position (0..749): "))
        if key < 0 or key > 749:
            print("Out of range. Must be 0..749.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    records = findRecords(dataDirectory, key)
    if not records:
        print(f"No records found at position {key}.")
    else:
        print(f"Records found at position {key}:")
        for i, rec in enumerate(records, start=1):
            print(f"\nRecord #{i}")
            print(f"Game ID: {rec.gameId}")
            print(f"Teams: {rec.teams}")
            print(f"Yards: {rec.yards}")
            print(f"Quarter: {rec.qtr}")
            if rec.date:
                print(f"Date: {rec.date.strftime('%Y-%m-%d')}")
            if rec.time:
                print(f"Time: {rec.time.strftime('%H:%M:%S')}")

if __name__ == "__main__":
    main()
