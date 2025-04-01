class Queue:
    def __init__(self):
        self.__data = []

    def isEmpty(self):
        return len(self.__data) == 0

    def enqueue(self, item):
        self.__data.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.__data.pop(0)
        return None
