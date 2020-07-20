import math 
import time 
import random
import statistics 

# Import the algorithms we want to test 
from src.a_star import * 
from src.a_star_variants import *

# Importing the map
from maze.diagrams import *


# Load the functions 
functions = a_star_search, bidirectional_a_star, weighted_a_star 
times = {f.__name__: [] for f in functions}

# Running the tests 
graph = diagram3
start, goal = (1, 4), (38, 28)

for i in range(3000):
    for _ in range(len(functions)):
        func = random.choice(functions)
        t0 = time.time()
        func(diagram3, start, goal)
        t1 = time.time()
        times[func.__name__].append((t1 - t0) * 1000)


for name, numbers in times.items():
    print('FUNCTION:', name, 'Used', len(numbers), 'times')
    print('\tMEDIAN', statistics.median(numbers))
    print('\tMEAN  ', statistics.mean(numbers))
    print('\tSTDEV ', statistics.stdev(numbers))