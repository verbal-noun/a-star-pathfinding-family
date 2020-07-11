from a_star import * 

# utility functions for the map 
def from_id_width(id, width):
    return (id % width, id // width)

# Function to draw proper  
def draw_tile(graph, id, style, width):
    # Default tile design 
    r = '.'
    # Draw the appropriate visual based on condition 
    if 'number' in style and id in style['number']: r  = "%d" % style['number'][id]
    if 'point_to' in style and style['point_to'].get(id, None) is not None:
        (x1, y1) = id
        (x2, y2) = style['point_to'][id]
        # Draw appropriate arrow relative to its parent 
        if x2 == x1 + 1: r = ">"
        if x2 == x1 - 1: r = "<"
        if y2 == y1 + 1: r = "v"
        if y2 == y1 - 1: r = "^"
    if 'start' in style and id == style['start']: r = "A"
    if 'goal' in style and id == style['goal']: r = "Z"
    if 'path' in style and id == style['path']: r = "@"
    if id in graph.walls: r = '#' * width

    # return the proper visual for the grid 
    return r 

# draw the map onto the screen 
def draw_grid(graph, width = 2, **style):
    for y in range(graph.height):
        for x in range(graph.width):
            print("%%-%ds" % width % draw_tile(graph, (x, y), style, width), end = "")
        print()


# Position of blocked tiles (walls) in the map 
DIAGRAM1_WALLS = [from_id_width(id, width=30) for id in [21,22,51,52,81,82,93,94,111,112,123,124,133,
134,141,142,153,154,163,164,171,172,173,174,175,183,184,193,194,201,202,203,
204,205,213,214,223,224,243,244,253,254,273,274,283,284,303,304,313,314,333,
334,343,344,373,374,403,404,433,434]]


# Implementation for weighted grid 
diagram4 = WeightedGrid(10, 10)
diagram4.walls = [(1, 7), (1, 8), (2, 7), (2, 8), (3, 7), (3, 8)]
diagram4.weights = {loc: 5 for loc in [(3, 4), (3, 5), (4, 1), (4, 2),
                                       (4, 3), (4, 4), (4, 5), (4, 6), 
                                       (4, 7), (4, 8), (5, 1), (5, 2),
                                       (5, 3), (5, 4), (5, 5), (5, 6), 
                                       (5, 7), (5, 8), (6, 2), (6, 3), 
                                       (6, 4), (6, 5), (6, 6), (6, 7), 
                                       (7, 3), (7, 4), (7, 5)]}




