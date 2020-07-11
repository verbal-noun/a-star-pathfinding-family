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