## README

## Project Description

This project is an assignment scheduled for the Data Structures course of the I Quarter 2025. The main objective is to work with overwriting special methods in Python and creating a `Comparator` class to compare objects. In addition, several sorting algorithms (bubble, insertion, merge sort and quicksort) are implemented to sort soccer plays (PUNT) based on different criteria.

The project is divided into two parts:
1. **Part One**: Sort PUNT plays by the amount of yards gained.
2. **Part Two**: Sort plays by date, quarter, distance traveled, and time.

## Requirements

- Python 3.x
- NFL play-by-play data files (available in the provided repository)

## Installation

1. Clone or download the repository with the NFL play-by-play data files from [here](https://github.com/ryurko/nflscrapR-data/tree/master/legacy_data/season_play_by_play).
2. Place all the downloaded files in a folder named ``dataprimeraprogramda''.
3. Make sure you have Python installed on your system.

## Execution

1. Open the project in Visual Studio Code.
2. Run the `.py` files corresponding to each part of the project.
3. The output files will be automatically generated in the results folder of the project, with names indicating the sorting algorithm used.
4. Execution times and statistics of comparisons and swaps will be printed on the console.

## Project Structure

- **Part One**: 
  - `dataReader.py`: Class to read and filter PUNT plays.
  - `puntPlay.py`: Class representing a PUNT play with overwritten comparison methods.

- **Part Two**:
  - `comparator.py`: Class to compare plays based on date, quarter, distance and time.