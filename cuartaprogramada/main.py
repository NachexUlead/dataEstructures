from generator import GeneratePeople
from queueSystem import Simulate
from metrics import CalculateMetrics, PrintMetrics

# Configuration
TOTAL_TIME = 480
LAMBDA_ARRIVAL = 1/2
LAMBDA_SERVICE = 1/4
PRIORITY_PROB = 0.3
NUM_STATIONS = 3

people = GeneratePeople(TOTAL_TIME, LAMBDA_ARRIVAL, PRIORITY_PROB, LAMBDA_SERVICE)

# Variant 1: All stations generic
served1, maxQueue1, usage1 = Simulate(people, NUM_STATIONS, "generic", TOTAL_TIME)
metrics1 = CalculateMetrics(served1, maxQueue1, usage1, TOTAL_TIME, NUM_STATIONS)
PrintMetrics("generic stations", metrics1)

# Variant 2: One station exclusive for priority
served2, maxQueue2, usage2 = Simulate(people, NUM_STATIONS, "exclusive", TOTAL_TIME)
metrics2 = CalculateMetrics(served2, maxQueue2, usage2, TOTAL_TIME, NUM_STATIONS)
PrintMetrics("1 exclusive station for priority", metrics2)
