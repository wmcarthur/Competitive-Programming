t = int(input())
def solve():
    n,m = map(int, input().split())
    s = [{} for __ in range(m)]
    for i in range(n):
        val = list(input())
        for j in range(m):
            if val[j] in s[j]:
                s[j][val[j]] += 1
            else:
                s[j][val[j]] = 1
    for i in range(n-1):
        val = list(input())
        for j in range(m):
            if s[j][val[j]] == 1:
                s[j].pop(val[j])
            else:
                s[j][val[j]] -= 1
    final = []
    for j in range(m):
        final.append(list(s[j].keys())[0])
    return final

for _ in range(t):
    print(''.join(solve()))