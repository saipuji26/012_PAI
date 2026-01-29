import heapq

def fuel_blend_astar(tankA, tankB, target_octane):
    heuristic = lambda a, b: abs(target_octane - a)

    operations = lambda a, b: [
        (tankA, b), (a, tankB),     # fill tanks
        (0, b), (a, 0),             # empty tanks
        (a - min(a, tankB - b), b + min(a, tankB - b)),  # A → B
        (a + min(b, tankA - a), b - min(b, tankA - a))   # B → A
    ]

    pq = [(0, 0, 0, [(0, 0)])]     # (f, A, B, path)
    visited = set()

    while pq:
        f, a, b, path = heapq.heappop(pq)

        if a == target_octane:
            return path

        if (a, b) in visited:
            continue
        visited.add((a, b))

        for na, nb in operations(a, b):
            if (na, nb) not in visited:
                g = len(path)
                h = heuristic(na, nb)
                heapq.heappush(pq, (g + h, na, nb, path + [(na, nb)]))

    return None


# Example: Fuel blending system
# Tank A = 7, Tank B = 4 → Target Octane = 6
result = fuel_blend_astar(7, 4, 6)
print(result)
