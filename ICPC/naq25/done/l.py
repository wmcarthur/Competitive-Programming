n = int(input())
d = list(map(int, input().split()))
bval = 0
for i in range(len(d)):
    if d[i] != d[0]:
        bval = d[i]
        break
a = d[0]//3
b = bval - a - a
c = d[-1]//3

# for val in d[1:-1]:
#     v = val - a - a
#     if v != a and v != c:
#         b = v
#         break
print(*[a,b,c])