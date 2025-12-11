n, k = map(int, input().split())
p = set()
t = 0
for _ in range(n):
    val = int(input())
    if val not in p:
        t += 1
        p.add(val)
print(min(t, k))