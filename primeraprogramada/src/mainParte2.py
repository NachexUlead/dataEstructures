from comparator import PlayComparator
from primeraprogramada.src.dataReader import DataReader
from sorting import Sorting
import time
import csv
import os

def executeAlgorithmP2(algorithm, playList, name):
    comparator = PlayComparator()
    start = time.time()
    
    if algorithm == Sorting.mergeSort:
        sortedList, _, _ = algorithm(playList.copy(), comparator=comparator)
    else:
        algorithm(playList.copy(), comparator=comparator)
        sortedList = playList.copy()
    
    end = time.time()
    
    print(f"\n{algorithm.__name__} (Part 2):")
    print(f"Start: {time.ctime(start)}")
    print(f"Duration: {end - start:.4f} sec")
    
    outputPath = f"../results/part2-{name}-result.csv"
    os.makedirs('../results', exist_ok=True)
    
    with open(outputPath, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Game ID", "Teams", "Yards", "Quarter", "Date", "Time"])
        for play in sortedList:
            writer.writerow(play.toCsvRow())

if __name__ == "__main__":
    reader = DataReader()
    plays = reader.readFiles(part=2)
    
    algorithms = {
        "bubble": Sorting.bubbleSort,
        "insertion": Sorting.insertionSort,
        "merge_sort": Sorting.mergeSort,
        "quicksort": Sorting.quickSort
    }
    
    for name, algo in algorithms.items():
        copy = plays.copy()
        executeAlgorithmP2(algo, copy, name)
