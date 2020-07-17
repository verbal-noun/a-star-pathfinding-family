import time 

# Importing a-star and family  
from src.a_star import * 
from src.a_star_variants import *
from src.other_algorithms import *

# Importing necessary diagrams and grid visualizer 
from maze.diagrams import *
from maze.grid import draw_grid

grid = diagram3

# #Testing a-star 
start, goal = (1, 4), (38, 28)
# Calculating the cost and node origins 
start_time = time.time()
path = a_star_search(grid, start, goal)
draw_grid(grid, width=3, path=path)
end_time = time.time() - start_time
print('TIme taken: %f\n' % end_time)
print('\n')


# Testing variants  
start_time = time.time()
path = bidirectional_a_star(grid, start, goal)
draw_grid(grid, width=3, path=path)
end_time = time.time() - start_time
print('TIme taken: %f\n' % end_time)

#draw_grid(diagram3, number=diagram3.weights)
#print(diagram1.walls)