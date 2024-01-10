#15..Lattice Paths
#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20×20 grid?

import math

def calculate_routes(grid_size):
    n = 2 * grid_size
    r = grid_size
    routes = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
    return routes

grid_size = 20
result = calculate_routes(grid_size)

print(result)

#output:137846528820
