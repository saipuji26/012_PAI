import heapq
A = int(input("Tank A: "))
B = int(input("Tank B: "))
T = int(input("Target: "))
pq = [(0, 0, 0, [(0, 0)])]
vis = set()
while pq:
    f, a, b, path = heapq.heappop(pq)
    if a == T:
        print("Solution:", path)
        break
    if (a, b) in vis:
        continue
    vis.add((a, b))
    for na, nb in [
        (A, b), (a, B), (0, b), (a, 0),
        (a - min(a, B-b), b + min(a, B-b)),
        (a + min(b, A-a), b - min(b, A-a))
    ]:
        if (na, nb) not in vis:
            heapq.heappush(pq, (len(path)+abs(T-na), na, nb, path+[(na, nb)]))
else:
    print("No solution")")
Output:-
Tank A: 4
Tank B: 3
Target: 2
Solution: [(0, 0), (0, 3), (3, 0), (3, 3), (4, 2), (0, 2), (2, 0)]
