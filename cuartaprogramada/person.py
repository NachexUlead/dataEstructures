class Person:
    def __init__(self, arrivalTime, priority, serviceTime):
        self.arrivalTime = arrivalTime
        self.priority = priority  # 0: high, 1: low
        self.serviceTime = serviceTime
        self.startServiceTime = None
        self.departureTime = None
