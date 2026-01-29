import heapq

def water_jug_astar(A, B, target):
    h = lambda x, y: min(abs(target - x), abs(target - y))
    moves = lambda x, y: [
        (A, y), (x, B), (0, y), (x, 0),
        (x - min(x, B - y), y + min(x, B - y)),
        (x + min(y, A - x), y - min(y, A - x))
    ]

    pq = [(0, 0, 0, [(0, 0)])]  # (f, x, y, path)
    visited = set()

    while pq:
        f, x, y, path = heapq.heappop(pq)
        if x == target or y == target:
            return path
        if (x, y) in visited:
            continue
        visited.add((x, y))

        for nx, ny in moves(x, y):
            if (nx, ny) not in visited:
                g = len(path)
                heapq.heappush(pq, (g + h(nx, ny), nx, ny, path + [(nx, ny)]))

    return None


# Example
print(water_jug_astar(4, 3, 2))
