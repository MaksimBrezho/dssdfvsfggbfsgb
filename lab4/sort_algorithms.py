import random

class SortAlgorithm:
    def __init__(self, array):
        self.array = array[:]

    def sort(self):
        raise NotImplementedError("Subclasses must implement sort method.")

    def fill_random(self):
        self.array = [random.randint(0, 1000) for _ in range(len(self.array))]

class SelectionSort(SortAlgorithm):
    def sort(self):
        n = len(self.array)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if self.array[j] < self.array[min_index]:
                    min_index = j
            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
            yield self.array

class QuickSort(SortAlgorithm):
    def sort(self):
        stack = [(0, len(self.array) - 1)]
        while stack:
            low, high = stack.pop()
            if low < high:
                pi = self._partition(low, high)
                if pi - 1 > low:
                    stack.append((low, pi - 1))
                if pi + 1 < high:
                    stack.append((pi + 1, high))
                yield self.array

    def _partition(self, low, high):
        pivot = self.array[high]
        i = low - 1
        for j in range(low, high):
            if self.array[j] <= pivot:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
        return i + 1

class InsertionSort(SortAlgorithm):
    def sort(self):
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i - 1
            while j >= 0 and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key
            yield self.array
