import math

def get_primes(n: int):
    factors = []

    # Handle factors of 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Handle odd factors
    # We only need to check up to the square root of n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    # If n is still greater than 2, it means it's a prime number itself
    if n > 2:
        factors.append(n)

    return factors


ranges = input().strip().split(',')
total = 0
used = set()
for rng in ranges:
    start, end = rng.split('-')
    l = int(start)
    r = int(end)
    if len(start) % 2 == 1 and len(end) % 2 == 1:
        pass
    
    print(start, "-", end)
    f = start[0]
    
    for length in range(1, len(end)):
        if len(start) == len(end):
            if len(end) % length != 0:
                continue
            print('length', length)
            f = 10**(length-1)
            # f = str(max(int(start[:length]), 10**(length-1)))
        
            valid = True
            while valid:
                print(f, type(f))
                val = f
                for i in range(len(end)//length - 1):
                    val += f
                print(val)
                if val in used:
                    f = str(int(f)+1)
                    continue
                if int(val) >= l and int(val) <= r:
                    total += int(val)
                    used.add(val)
                    print("S", val)
                elif int(val) > r:
                    valid = False
                f = str(int(f)+1)
                print()
        else:
            if len(end) % length == 0:
                
                print('length', length)
                f = 10**(length-1)
                # f = str(max(int(start[:length]), 10**(length-1)))
                valid = True
                while valid:
                    # print(f, type(f))
                    val = f
                    for i in range(len(end)//length - 1):
                        val += f
                    print(val)
                    if val in used:
                        f = str(int(f)+1)
                        continue
                    if int(val) >= l and int(val) <= r:
                        total += int(val)
                        used.add(val)
                        print("S", val)
                    elif int(val) > r:
                        valid = False
                    f = str(int(f)+1)
                    print()
            if len(start) % length == 0:
                
                print('length', length)
                f = 10**(length-1)
                # f = str(max(int(start[:length]), 10**(length-1)))
                valid = True
                while valid:
                    print(f, type(f))
                    val = f
                    for i in range(len(start)//length - 1):
                        val += f
                    print(val)
                    if val in used:
                        f = str(int(f)+1)
                        continue
                    if int(val) >= l and int(val) <= r:
                        total += int(val)
                        used.add(val)
                        print("S", val)
                    elif int(val) > r:
                        valid = False
                    f = str(int(f)+1)
                    print()
        
print(total)
