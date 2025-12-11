t = int(input())
def solve():
    p = list(input())
    s = list(input())
    curr = 'L'
    min = 0
    pCounts = []
    for char in p:
        if char == curr:
            min += 1
        else:
            pCounts.append(min)
            min = 1
            if curr == 'L': curr = 'R'
            else: curr = 'L'
    pCounts.append(min)
    # print(counts, p, s)
    curr = 'L'
    min = 0
    sCounts = []
    for char in s:
        if char == curr:
            min += 1
        else:
            sCounts.append(min)
            min = 1
            if curr == 'L': curr = 'R'
            else: curr = 'L'
    sCounts.append(min)
    print(pCounts, sCounts)

    if len(sCounts) != len(pCounts): return False
    if (pCounts[0] ^ sCounts[0]) == 1: return False
    for i in range(len(pCounts)):
        if (sCounts[i] < pCounts[i]) or (sCounts[i] > 2 * pCounts[i]): return False
    return True

for _ in range(t):
    if solve():
        print("YES")
    else:
        print("NO")