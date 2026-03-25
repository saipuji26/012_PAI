import heapq
def water_jug_astar(A, B, target):
    h = lambda x, y: min(abs(target - x), abs(target - y))
    def moves(x, y):
        return [
            (A, y), (x, B), (0, y), (x, 0),
            (x - min(x, B - y), y + min(x, B - y)),
            (x + min(y, A - x), y - min(y, A - x))
        ]
    pq = [(0, 0, 0, [(0, 0)])]
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
A = int(input("Enter capacity of jug 1: "))
B = int(input("Enter capacity of jug 2: "))
target = int(input("Enter target: "))
result = water_jug_astar(A, B, target)
if result:
    print("Path:", result)
else:
    print("No solution")
    
OUTPUT:-
Enter capacity of jug 1: 4
Enter capacity of jug 2: 3
Enter target: 2
Path: [(0, 0), (0, 3), (3, 0), (3, 3), (4, 2)]
