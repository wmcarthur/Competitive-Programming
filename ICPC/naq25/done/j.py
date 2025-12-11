n = list(map(int, input().split()))
p = n[-1] % 10
if p == 0:
    p = 10
print(p)