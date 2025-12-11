n = int(input())
c = [i**3 for i in range(1, 100000000)]
m = set()
for val in c:
    if (val - n) in m:
        print(int(val ** (1/3)) + 1, int((val - n)**(1/3))+1)
        break
    m.add(val)
else:
    print(-1)