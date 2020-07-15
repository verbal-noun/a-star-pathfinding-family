# Structure of the graph which we will traverse  
class SimpleGraph:
    def __init__(self):
        self.edges = {}

    def neighbors(self, id):
        return self.edges[id]


# Sample implementation of the graph we made 
example_graph = SimpleGraph()
example_graph.edges = {
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['A'],
    'D': ['E', 'A'],
    'E': ['B']
}

# Implementation of the queue going to be used for BFS 
import collections

# This queue class is just a wrapper around deque class 
class Queue: 
    def __init__(self):
        self.elements = collections.deque(); 

    def isEmpty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)
    
    def get(self):
        return self.elements.popleft()

"""
SquareGrid class - map representation  
Holds location tuples (int, int) -> (x, y)

This grid cells does not have weights 
"""
class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

    # Method to check if location is within the map 
    def in_bounds(self, id):
        (x, y) = id; 
        return 0 <= x < self.width and 0 <= y < self.height 

    # Check if current location is blocked for not 
    def passable(self, id):
        return id not in self.walls

    # Check the neighbors of the current grid 
    def neighbors(self, id): 
        (x, y) = id
        result = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        # Just for aesthetics 
        if(x + y) % 2 == 0: 
            result.reverse()
        # Check if the neighbors are in the map and not blocked 
        result = filter(self.in_bounds, result)
        result = filter(self.passable, result)

        return result


""" 
A Class which also can represent the cost of movement
Extends the SquareGrid class to add extra functionality 

"""
class WeightedGrid(SquareGrid):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.weights = {}

    # Method to get cost to travel from weights, else default value 
    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)


# Implementing a priority queue with heaps 
import heapq 

# Wrapper class with added functionalities 
class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def isEmpty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        # Return only the item 
        return heapq.heappop(self.elements)[1]


# Function to reconstruct path from start to goal using the source dictionary 
def reconstruct_path(came_from, start, goal):
    current = goal 
    path = []

    while current != start:
        path.append(current)
        current = came_from[current]

    # Add the start to the path - optional 
    path.append(start)
    # reverse the path to get from start to goal 
    path.reverse()
    return path

# Combine two paths and avoid happing overlapping nodes 
def join_paths(path_1, path_2):
    path_2.reverse() 
    if(path_1[-1] == path_2[0]):
        return path_1 + path_2[1:]


# The heuristic used by the a-star algorithm 
# This is used to calculate the distance of current node form the goal too 
def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b

    return abs(x1 - x2) + abs(y1 - y2)

# Implementation of the a-star search algorithm 
def a_star_search(graph, start, goal):
    # Priority Queue track progression of nodes 
    frontier = PriorityQueue()
    frontier.put(start, 0)
    
    # Dictionary to track origin of a node 
    came_from = {}
    # Dictionary to track the cost to move to a particular node 
    cost_so_far = {}

    # Add starting node into the dictionaries 
    came_from[start] = None
    cost_so_far[start] = 0 

    # While the Priority queue is not empty 
    while not frontier.isEmpty():
        # Get the top of queue 
        current = frontier.get()

        # check if we have reached destination 
        if current == goal: 
            break 

        # Loop through neighbors of current node and process them 
        for next in graph.neighbors(current):
            # Calculate the new cost to travel to neighboring node 
            # The new cost is cost of travelling to current node plus the cost of
            # travelling from current node to the neighbor 
            new_cost = cost_so_far[current] + graph.cost(current, next)
            
            # Check if this node hasn't been reached before or we have a new cheaper path
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                # Set the priority of the neighbor using the heuristic 
                # We are taking distance to goal in consideration through heuristics 
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current

    
    # Return the cost and source dictionary 
    #return came_from, cost_so_far
    return reconstruct_path(came_from, start, goal)


# Implementation of bidirectional a-start
# This algorithm will start looking for a path from both the start and the goal 
def bidirectional_a_star(graph, start, goal):
    # Priority queues to hold the progression of nodes 
    # This will hold nodes starting from the 'start' node 
    frontier_1 = PriorityQueue()
    frontier_1.put(start, 0)
    # This will node nodes starting from the 'goal' node 
    frontier_2 = PriorityQueue()
    frontier_2.put(goal, 0)

    # Dictionaries to hold the cost of travel and origin of nodes 
    # For the start node 
    came_from_1 = {}
    cost_so_far_1 = {}

    came_from_1[start] = None 
    cost_so_far_1[start] = 0 


    # For the goal node 
    came_from_2 = {}
    cost_so_far_2 = {}

    came_from_2[goal] = None
    cost_so_far_2[goal] = 0 

    # Run the loop until both of the 
    while not frontier_1.isEmpty() or frontier_2.isEmpty():
        # Get the top from each of the queues 
        current_1 = frontier_1.get()
        current_2 = frontier_2.get()

        #Check if we have found a full path or not 
        if current_1 == goal or current_2 == start: 
            break 
        # We have found two overlapping node 
        if current_1 in cost_so_far_2 and current_2 in cost_so_far_1:
            path_1 = reconstruct_path(came_from_1, start, current_1) 
            path_2 = reconstruct_path(came_from_2, goal, current_2)
            combined_path = join_paths(path_1, path_2)
            break
        # Only one of the nodes are are overlapping 
        elif (current_1 in cost_so_far_2):
            path_1 = reconstruct_path(came_from_1, start, current_1) 
            path_2 = reconstruct_path(came_from_2, goal, current_1)
            combined_path = join_paths(path_1, path_2)
            break 

        elif (current_2 in cost_so_far_1):
            path_1 = reconstruct_path(came_from_1, start, current_2) 
            path_2 = reconstruct_path(came_from_2, goal, current_2)
            combined_path = join_paths(path_1, path_2)
            break
        
        
        # A detailed description of the steps can be found in the implementation of 
        # a_star_search function 
        # Process the nodes from the start side 
        for next in graph.neighbors(current_1): 
            new_cost = cost_so_far_1[current_1] + graph.cost(current_1, next)

            if next not in cost_so_far_1 or new_cost < cost_so_far_1[next]:
                cost_so_far_1[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier_1.put(next, priority)
                came_from_1[next] = current_1

        # Process the nodes from the goal side 
        for next in graph.neighbors(current_2): 
            new_cost = cost_so_far_2[current_2] + graph.cost(current_2, next)

            if next not in cost_so_far_2 or new_cost < cost_so_far_2[next]:
                cost_so_far_2[next] = new_cost
                priority = new_cost + heuristic(start, next)
                frontier_2.put(next, priority)
                came_from_2[next] = current_2


    return combined_path