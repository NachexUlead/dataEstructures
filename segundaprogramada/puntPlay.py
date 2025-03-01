import csv
import time
from datetime import datetime


class PuntPlay:
    def __init__(self, game_id, teams, yards, qtr, date=None, time_str=None):
        self.gameId = game_id
        self.teams = teams
        self.yards = self._convertToInt(yards)
        self.qtr = self._convertToInt(qtr)
        self.date = self._parseDate(date)
        self.time = self._parseTime(time_str)

    @staticmethod
    def _convertToInt(value, default=0):
        """Converts a value to an integer, handling empty or invalid values."""
        try:
            return int(value) if value else default
        except ValueError:
            return default

    @staticmethod
    def _parseDate(dateStr):
        """Converts a string to a date (YYYY-MM-DD)."""
        try:
            return datetime.strptime(dateStr, "%Y-%m-%d") if dateStr else None
        except ValueError:
            print(f"Invalid date: {dateStr}")
            return None

    @staticmethod
    def _parseTime(timeStr):
        """Converts a string to a time object, handling multiple formats."""
        if not timeStr:
            return None
        for fmt in ("%H:%M:%S", "%M:%S"):
            try:
                return datetime.strptime(timeStr, fmt).time()
            except ValueError:
                continue
        print(f"Invalid time format: {timeStr}")
        return None

    def __eq__(self, other):
        return self.yards == other.yards

    def __lt__(self, other):
        return self.yards < other.yards

    def __gt__(self, other):
        return self.yards > other.yards

    def toCsvRow(self):
        return [
            self.gameId,
            self.teams,
            str(self.yards),
            str(self.qtr),
            self.date.strftime("%Y-%m-%d") if self.date else "",
            self.time.strftime("%H:%M:%S") if self.time else "",
        ]
