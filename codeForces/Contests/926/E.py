n = int(input())
a = list(map(int, input().split()))
b = [a[0]]
last = a[0]
for i in range(1, n, 1):
    av = a[i]
    b.append(av)
    while len(b) > 1 and b[-2] == b[-1]:
        b.pop()
        b[-1] += 1
print(len(b))
print(*b)