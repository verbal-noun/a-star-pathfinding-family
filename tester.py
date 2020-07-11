from a_star import * 
from grid import * 

def bfs_1(graph, start, goal):
    # We will print what we find 
    frontier = Queue()
    frontier.put(start)
    # Dictionary to hold the visited nodes and their source 
    came_from = {}
    came_from[start] = None

    # Perfrom the breadth first search 
    while not frontier.isEmpty():
        current = frontier.get()

        # Check if goal is reached or not 
        if current == goal: 
            break 
        # Check for neighbors 
        for next in graph.neighbors(current): 
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
    
    return came_from


g = SquareGrid(30, 15)
g.walls = DIAGRAM1_WALLS  

parents  = bfs_1(g, (8, 7), (17, 2))
draw_grid(g, width=2, point_to=parents, start=(8,7), goal=(17, 2))