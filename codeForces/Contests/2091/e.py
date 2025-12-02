t = int(input())
maxN = 10000001
prime = [0,0] + [1 for _ in range(maxN-2)]
for i in range(2, int(maxN**0.5) + 1):
    if not prime[i]: continue
    for j in range(i*i, maxN, i):
        prime[j] = 0
 
for _ in range(t):
    n = int(input())
    count = 0
    for i in range(n+1):
        if prime[i]: count += n//i
    print(count)