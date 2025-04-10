def Simulate(people, numStations, systemType, totalTime):
    time = 0
    priorityQueue = []
    normalQueue = []
    stations = [None] * numStations
    occupation = [0.0] * numStations
    maxQueueLength = 0
    servedPeople = []

    people.sort(key=lambda p: p.arrivalTime)
    pending = list(people)

    while time < totalTime or any(stations) or pending:
        while pending and pending[0].arrivalTime <= time:
            person = pending.pop(0)
            if person.priority == 0:
                priorityQueue.append(person)
            else:
                normalQueue.append(person)

        for i in range(numStations):
            if stations[i] is None:
                if systemType == "exclusive" and i == 0:
                    if priorityQueue:
                        p = priorityQueue.pop(0)
                    elif normalQueue:
                        p = normalQueue.pop(0)
                    else:
                        continue
                else:
                    if priorityQueue:
                        p = priorityQueue.pop(0)
                    elif normalQueue:
                        p = normalQueue.pop(0)
                    else:
                        continue

                p.startServiceTime = time
                p.departureTime = time + p.serviceTime
                stations[i] = p
                occupation[i] += p.serviceTime

        for i in range(numStations):
            p = stations[i]
            if p and p.departureTime <= time:
                servedPeople.append(p)
                stations[i] = None

        maxQueueLength = max(maxQueueLength, len(priorityQueue) + len(normalQueue))
        time += 1

    return servedPeople, maxQueueLength, occupation
