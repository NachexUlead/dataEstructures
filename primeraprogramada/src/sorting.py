class Sorting:
    @staticmethod
    def bubbleSort(list, comparator=None, count=False):
        n = len(list)
        comparisons = 0
        swaps = 0

        for i in range(n - 1):
            for j in range(n - 1 - i):
                comparisons += 1
                if comparator:
                    result = comparator.compare(list[j], list[j + 1])
                    condition = result == 1
                else:
                    condition = list[j] < list[j + 1]

                if condition:
                    list[j], list[j + 1] = list[j + 1], list[j]
                    swaps += 1
        return (comparisons, swaps) if count else None

    @staticmethod
    def insertionSort(list, comparator=None, count=False):
        comparisons = 0
        swaps = 0
        for i in range(1, len(list)):
            key = list[i]
            j = i - 1
            while j >= 0:
                comparisons += 1
                if comparator:
                    result = comparator.compare(key, list[j])
                    condition = result == 1
                else:
                    condition = key > list[j]

                if condition:
                    list[j + 1] = list[j]
                    swaps += 1
                    j -= 1
                else:
                    break
            list[j + 1] = key
        return (comparisons, swaps) if count else None

    @staticmethod
    def mergeSort(list, comparator=None, count=False):
        def merge(left, right):
            merged = []
            i = j = 0
            comparisons = 0
            swaps = 0

            while i < len(left) and j < len(right):
                if comparator:
                    result = comparator.compare(left[i], right[j])
                    condition = result == 1
                else:
                    condition = left[i] > right[j]

                comparisons += 1
                if condition:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
                swaps += 1

            merged += left[i:]
            merged += right[j:]
            return merged, comparisons, swaps

        if len(list) <= 1:
            return (list, 0, 0) if count else (list, 0, 0)

        mid = len(list) // 2
        left, compLeft, swapsLeft = Sorting.mergeSort(list[:mid], comparator, count)
        right, compRight, swapsRight = Sorting.mergeSort(list[mid:], comparator, count)

        merged, compMerge, swapsMerge = merge(left, right)
        totalComparisons = compLeft + compRight + compMerge
        totalSwaps = swapsLeft + swapsRight + swapsMerge

        return (merged, totalComparisons, totalSwaps) if count else (merged, 0, 0)

    @staticmethod
    def quickSort(list, comparator=None, count=False):
        def _partition(low, high):
            pivot = list[high]
            i = low - 1
            comparisons = 0
            swaps = 0

            for j in range(low, high):
                comparisons += 1
                if comparator:
                    result = comparator.compare(list[j], pivot)
                    condition = result == 1
                else:
                    condition = list[j] > pivot

                if condition:
                    i += 1
                    list[i], list[j] = list[j], list[i]
                    swaps += 1

            list[i + 1], list[high] = list[high], list[i + 1]
            swaps += 1
            return i + 1, comparisons, swaps

        stack = []
        totalComparisons = 0
        totalSwaps = 0

        stack.append((0, len(list) - 1))

        while stack:
            low, high = stack.pop()
            if low < high:
                pivotIndex, partComparisons, partSwaps = _partition(low, high)
                totalComparisons += partComparisons
                totalSwaps += partSwaps

                if pivotIndex - low < high - pivotIndex:
                    stack.append((pivotIndex + 1, high))
                    stack.append((low, pivotIndex - 1))
                else:
                    stack.append((low, pivotIndex - 1))
                    stack.append((pivotIndex + 1, high))

        return (totalComparisons, totalSwaps) if count else None