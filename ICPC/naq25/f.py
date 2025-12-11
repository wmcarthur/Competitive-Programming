n,k = map(int, input().split())
minbad = 1000000
scores = [float(input()) for _ in range(n)]
scores = sorted(scores)

# Prefix sum
pf = [0] * (n + 1)

for i in range(1,n+1):
    pf[i] = pf[i-1] + scores[i-1]

# Calculate each window
for i in range(k, n+1):
    total = pf[i] - pf[i-k]
    mean = float(total) / float(k)
    badness = 0
    for j in range(i-k, i):
        # print(j)
        badness += (mean-scores[j])**2
    minbad = min(minbad, badness)
    # print(badness)

print(minbad)