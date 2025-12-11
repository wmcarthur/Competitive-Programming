from collections import deque
n, m  = map(int, input().split())
 
ally = {}
for i in range(1, n+1):
    ally[i] = set()
 
for _ in range(m):
    a, b = map(int, input().split())
 
    ally[a].add(b)
    ally[b].add(a)

# print(ally)
q = deque()
 
for i in range(1, n+1):
    if len(ally[i]) < 3:
        q.append(i)

t = 0

while len(q):
    # print(q)
    idx = q.pop()

    allies = ally[idx]
    if len(allies) >=3:
        continue
    t += 1

    for val in allies:
        if val not in q:
            q.append(val)
        ally[val].remove(idx)
        # print(ally)

print(t)