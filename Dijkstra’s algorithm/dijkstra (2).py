graph = {}
graph["start"] = {}
graph["start"]["a"] = 10
graph["start"]["b"] = 5
graph["start"]["c"] = 2

graph["a"] = {}
graph["a"]["fin"] = 50
graph["a"]["b"] = 5

graph["b"] = {}
graph["b"]["fin"] = 20

graph["c"] = {}
graph["c"]["d"] = 1
graph["c"]["b"] = 1

graph["d"] = {}
graph["d"]["b"] = 1
graph["d"]["fin"] = 30

graph["fin"] = {}


infinity = float("inf")
costs = {}
costs["a"] = 10
costs["b"] = 5
costs["c"] = 2
costs["d"] = infinity
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = "start"
parents["d"] = None
parents["fin"] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_node = node
    return lowest_node

node = find_lowest_cost_node(costs)

while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(costs["fin"])