n = int(input())
idcs = input().split()
idcs = [int(idcs[i]) for i in range(len(idcs))]
newIds = []
cont = set()
for i in range(n - 1, -1, -1):
    val = idcs[i]
    if val in cont:
        pass
    else:
        cont.add(val)
        newIds.append(val)
print(newIds[len(newIds) - 1])
    