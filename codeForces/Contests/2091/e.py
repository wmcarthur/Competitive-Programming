import math
t = int(input())
primes = set()
def prime(n):
    if n in primes: return True
    if n < 2: return False
    if n < 4: return True
    if n%2 == 0 or n % 3 == 0: return False
    i = 5
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    primes.add(n)
    return True

for _ in range(t):
    n = int(input())
    count = 0
    for i in range(n):
        for j in range(i+1, n+1):
            d = math.gcd(i, j)
            count += prime(((i*j)//d)//d)
    print(count)