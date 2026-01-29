import heapq

def water_jug_astar(A, B, target):
    h = lambda x, y: abs(target - x)
    moves = lambda x, y: [
        (A, y), (x, B), (0, y), (x, 0),
        (x - min(x, B - y), y + min(x, B - y)),
        (x + min(y, A - x), y - min(y, A - x))
    ]

    pq = [(0, 0, 0, [(0, 0)])]
    visited = set()

    while pq:
        f, x, y, path = heapq.heappop(pq)
        if x == target:
            return path
        if (x, y) in visited:
            continue
        visited.add((x, y))

        for nx, ny in moves(x, y):
            if (nx, ny) not in visited:
                g = len(path)
                heapq.heappush(pq, (g + h(nx, ny), nx, ny, path + [(nx, ny)]))

    return None


# Space station problem
result = water_jug_astar(7, 4, 6)
print(result)
