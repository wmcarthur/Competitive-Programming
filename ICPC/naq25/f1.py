n,k = map(int, input().split())
minbad = float('inf')
scores = [float(input()) for _ in range(n)]
scores = sorted(scores)

# Prefix sum
pf = [0.0] * (n + 1)
sqpf = [0.0] * (n + 1)

for i in range(1,n+1):
    pf[i] = pf[i-1] + scores[i-1]
    sqpf[i] = sqpf[i-1] + scores[i-1]**2

# Calculate each window
for i in range(k, n+1):
    l = i-k
    u = i
    total = pf[u] - pf[l]
    sqtotal = sqpf[u] - sqpf[l]
    mean = float(total) / float(k)
    badness = sqtotal - 2*mean*total + k*mean**2
    minbad = min(minbad, badness)

print(minbad)