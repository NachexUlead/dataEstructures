import numpy as np
import random
from person import Person

def GeneratePeople(totalTime, lambdaArrival, priorityProb, lambdaService):
    people = []
    currentTime = 0.0
    while currentTime < totalTime:
        timeBetweenArrivals = np.random.exponential(1 / lambdaArrival)
        currentTime += timeBetweenArrivals

        if currentTime >= totalTime:
            break

        priority = 0 if random.random() < priorityProb else 1
        serviceTime = np.random.exponential(1 / lambdaService)
        people.append(Person(currentTime, priority, serviceTime))

    return people
