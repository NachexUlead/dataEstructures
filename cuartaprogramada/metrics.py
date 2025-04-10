def CalculateMetrics(servedPeople, maxQueueLength, occupation, totalTime, numStations):
    waitTimes = [p.startServiceTime - p.arrivalTime for p in servedPeople]
    avgWaitTime = sum(waitTimes) / len(waitTimes) if waitTimes else 0
    totalUsage = sum(occupation)
    utilizationRate = (totalUsage / (totalTime * numStations)) * 100

    return {
        "avgWaitTime": avgWaitTime,
        "maxQueueLength": maxQueueLength,
        "utilization": utilizationRate
    }

def PrintMetrics(name, metrics):
    print(f"\nSimulation with {name}:")
    print(f"Average wait time: {metrics['avgWaitTime']:.2f} min")
    print(f"Max queue length: {metrics['maxQueueLength']}")
    print(f"Utilization: {metrics['utilization']:.2f}%")
