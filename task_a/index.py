import itertools


routes = [
    #A  B   C   D   E   F
    [0, 10, 15, 20, 25, 30], # A 
    [10, 0, 35, 25, 17, 28], # B
    [15, 35, 0, 30, 28, 40], # C
    [20, 25, 30, 0, 22, 16], # D
    [25, 17, 28, 22, 0, 35], # E
    [38, 28, 40, 16, 35, 0], # F
]



def fact(n):
    if n == 1 or n == 0:
        return n
    return  n * fact(n-1)

miniumum_cost = 0
route_costs = []
possible_routes = {}
number_of_possible_routes = fact(len(routes))

num_of_nodes = len(routes)
vertices = list(range(num_of_nodes))
vertices.remove(0)


perm = itertools.permutations(vertices)
for p in perm:

    cost = 0
    k = 0 
    for i in p:
        cost += routes[k][i]
        k = i
    possible_routes[str(cost)] = (0, ) + p + (0,)

min_cost = min(possible_routes.keys())

shortest_route_in_tuple = possible_routes[min_cost]
shortest_route_in_str = ""

for i in shortest_route_in_tuple:
    if i == 0:
        shortest_route_in_str += "A->"
    elif i == 1:
        shortest_route_in_str += "B->"
    elif i == 2:
        shortest_route_in_str += "C->"
    elif i == 3:
        shortest_route_in_str += "D->"
    elif i == 4:
        shortest_route_in_str += "E->"
    elif i == 5:
        shortest_route_in_str += "F->"

shortest_route_in_str.rstrip("->")

print(f"Shortest route is {shortest_route_in_str} with distance {min_cost}")