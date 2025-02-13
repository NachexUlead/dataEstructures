from puntPlay import PuntPlay
from dataReader import DataReader
from sorting import Sorting
import time
import csv
import os


def executeAlgorithm(algorithm, playList, name):
    start = time.time()

    if algorithm == Sorting.mergeSort:
        sortedList, comparisons, swaps = algorithm(playList.copy(), count=True)
    else:
        comparisons, swaps = algorithm(playList.copy(), count=True)
        sortedList = playList.copy()

    end = time.time()

    print(f"\n{algorithm.__name__}:")
    print(f"Start: {time.ctime(start)}")
    print(f"Duration: {end - start:.4f} sec")
    print(f"Comparisons: {comparisons}")
    print(f"Swaps: {swaps}")

    outputPath = f"../results/part1-{name}-result.csv"
    os.makedirs('../results', exist_ok=True)

    with open(outputPath, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Game ID", "Teams", "Yards", "Quarter"])
        for play in sortedList:
            writer.writerow(play.toCsvRow()[:4])


if __name__ == "__main__":
    reader = DataReader()
    plays = reader.readFiles(part=1)
    print(f"Total loaded plays: {len(plays)}")
    if plays:
        print("First element:", plays[0].toCsvRow())

    algorithms = {
        "bubble": Sorting.bubbleSort,
        "insertion": Sorting.insertionSort,
        "merge_sort": Sorting.mergeSort,
        "quicksort": Sorting.quickSort
    }

    for name, algo in algorithms.items():
        copy = plays.copy()
        executeAlgorithm(algo, copy, name)
