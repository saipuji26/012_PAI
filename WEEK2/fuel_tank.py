import heapq
def fuel_blend_astar(tankA, tankB, target_octane):
    heuristic = lambda a, b: abs(target_octane - a)
    operations = lambda a, b: [
        (tankA, b), (a, tankB),     
        (0, b), (a, 0),             
        (a - min(a, tankB - b), b + min(a, tankB - b)),  
        (a + min(b, tankA - a), b - min(b, tankA - a))   
    ]
    pq = [(0, 0, 0, [(0, 0)])]   
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
result = fuel_blend_astar(7, 4, 6)
print(result)

