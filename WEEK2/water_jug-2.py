import heapq
def solve():
    A = int(input("Jug A: "))
    B = int(input("Jug B: "))
    T = int(input("Target: "))
    h = lambda x: abs(T - x)
    pq = [(0, 0, 0, [(0, 0)])]
    visited = set()
    while pq:
        f, x, y, path = heapq.heappop(pq)
        if x == T:
            print("Solution:", path)
            return
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for nx, ny in [
            (A, y), (x, B), (0, y), (x, 0),
            (x - min(x, B-y), y + min(x, B-y)),
            (x + min(y, A-x), y - min(y, A-x))
        ]:
            if (nx, ny) not in visited:
                heapq.heappush(pq, (len(path)+h(nx), nx, ny, path+[(nx, ny)]))
    print("No solution")
solve()
print(result)
OUTPUT:-
Jug A: 4
Jug B: 3
Target: 2
Solution: [(0, 0), (0, 3), (3, 0), (3, 3), (4, 2), (0, 2), (2, 0)]
