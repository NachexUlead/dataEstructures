import os
import csv
from datetime import datetime
from puntPlay import PuntPlay


class DataReader:
    def __init__(self, folderPath='../dataprimeraprogramada'):
        self.folderPath = folderPath
        if not os.path.exists(folderPath):
            raise FileNotFoundError(
                f"The directory {folderPath} does not exist")

        self.columns = {
            "desc": "desc",
            "fumble": "Fumble",
            "gameId": "GameID",
            "awayTeam": "AwayTeam",
            "homeTeam": "HomeTeam",
            "yards": "Yards.Gained",
            "quarter": "qtr",
            "date": "Date",
            "time": "time"
        }

    def _meetsConditions(self, desc, fumble):
        """Checks if it is a punt without a fumble (case-insensitive)"""
        desc = desc.strip().lower()
        return "punt" in desc and fumble.strip() == "0"

    def readFiles(self, part=1):
        """Reads and processes all CSV files using column names"""
        puntPlays = []
        print(f'\nReading files from: {os.path.abspath(self.folderPath)}')

        for filename in os.listdir(self.folderPath):
            if not filename.endswith(".csv"):
                continue

            fullPath = os.path.join(self.folderPath, filename)
            print(f"\nProcessing: {filename}")

            try:
                with open(fullPath, 'r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)

                    missingColumns = [
                        col for col in self.columns.values() if col not in reader.fieldnames]
                    if missingColumns:
                        print(
                            f"Warning! {filename} is missing required columns: {missingColumns}")
                        continue

                    for rowIndex, row in enumerate(reader):
                        try:
                            desc = row[self.columns["desc"]]
                            fumble = row[self.columns["fumble"]]

                            if rowIndex < 3:
                                print(
                                    f"[Row {rowIndex}] Desc: {desc[:30]}... | Fumble: {fumble}")

                            if self._meetsConditions(desc, fumble):
                                gameId = row[self.columns["gameId"]]
                                awayTeam = row[self.columns["awayTeam"]]
                                homeTeam = row[self.columns["homeTeam"]]
                                yards = row[self.columns["yards"]]
                                quarter = row[self.columns["quarter"]]

                                play = PuntPlay(
                                    game_id=gameId,
                                    teams=f"{awayTeam} @ {homeTeam}",
                                    yards=yards,
                                    qtr=quarter,
                                    date=row[self.columns["date"]
                                             ] if part == 2 else None,
                                    time_str=row[self.columns["time"]
                                                 ] if part == 2 else None
                                )

                                puntPlays.append(play)
                                if len(puntPlays) % 100 == 0:
                                    print(
                                        f"Loaded plays: {len(puntPlays)}")

                        except Exception as e:
                            print(f"Error in row {rowIndex}: {str(e)}")
                            continue

            except Exception as e:
                print(f"Error opening {filename}: {str(e)}")
                continue

        print(f"\nTotal valid plays: {len(puntPlays)}")
        return puntPlays
