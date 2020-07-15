from a_star import * 
from grid import * 
from other_algorithms import *


g = SquareGrid(30, 15)
g.walls = DIAGRAM1_WALLS  

#parents  = bfs_search(g, (8, 7), (17, 2))
#draw_grid(g, width=2, point_to=parents, start=(8,7), goal=(17, 2))
came_from, cost_so_far = dijkstra_search(diagram4, (1, 4), (7, 8))
# draw_grid(diagram4, width=3, point_to=came_from, start=(1, 4), goal=(7, 8))
# print()
# draw_grid(diagram4, width=3, number=cost_so_far, start=(1, 4), goal=(7, 8))
# print()
draw_grid(diagram4, width=3, path=reconstruct_path(came_from, start=(1, 4), goal=(7, 8)))
print()


# Testing a-start 
start, goal = (1, 4), (7, 8)
# Calculating the cost and node origins 
came_from, cost_so_far = a_star_search(diagram4, start, goal)
draw_grid(diagram4, width=3, path=reconstruct_path(came_from, start, goal))