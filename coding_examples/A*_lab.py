import heapq

def a_star(graph, start, goal, heuristic):

    OPEN = []
    CLOSED = set()

    g = {start: 0}
    parent = {start: None}

    heapq.heappush(OPEN, (heuristic[start], start))

    while OPEN:

        f, n = heapq.heappop(OPEN)

        if n in CLOSED:
            continue

        CLOSED.add(n)

        if n == goal:
            path = []
            while n is not None:
                path.append(n)
                n = parent[n]

            return path[::-1], g[goal]

        for m, cost in graph[n].items():

            new_g = g[n] + cost

            if m not in g or new_g < g[m]:

                g[m] = new_g
                parent[m] = n

                heapq.heappush(
                    OPEN,
                    (g[m] + heuristic[m], m)
                )

    return None, float('inf')


# Graph representation
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'D': 4},
    'C': {'D': 2},
    'D': {}
}

# Heuristic values
heuristic = {
    'A': 4,
    'B': 3,
    'C': 2,
    'D': 0
}

start = 'A'
goal = 'D'

path, cost = a_star(graph, start, goal, heuristic)

print("Path:", path)
print("Cost:", cost)
