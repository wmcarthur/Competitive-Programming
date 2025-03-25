import heapq
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    adj = [[] for i in range(n+1)]
    roads = []
    visited = set()
    distances = {}
    for i in range(m):
        u,v,w = map(int,input().split())
        u -= 1; v-= 1
        adj[u].append(v); adj[v].append(u); roads.append(w)
    bikes = list(map(int,input().split()))

    q = [] #Hold time, city, speed
    heapq.heappush(q, (0, 0, bikes[0]))

    while q:
        time, city, speed = heapq.heappop(q)
        
        visited.add(city)
        if city not in distances: distances[city] = time
        elif distances[city] < time: continue

        if city == n-1: print("time:",time)

        for neighbor in adj[city]:
            if neighbor in visited: continue
            heapq.heappush(q, (time+(speed*roads[city]), neighbor, min(speed, bikes[neighbor])))
