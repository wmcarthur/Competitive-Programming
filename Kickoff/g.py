n,q = map(int, input().split())

t1 = {} #mile to name
t2 = {} #name to mile

for _ in range(n):
    i = input().split()
    t2[i[0]] = int(i[1])
    t1[i[1]] = i[0]

for _ in range(q):
    i = input().split()
    t = int(i[0])
    if t == 1:
        print(t1[i[1]])
    else:
        print(t2[i[1]])