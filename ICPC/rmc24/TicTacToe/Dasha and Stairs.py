line = input().split()
even = int(line[0])
odd = int(line[1])

if even == 0 and odd == 0:
    print("NO")
else:
    if abs(even - odd) <= 1:
        print("YES")
    else:
        print("NO")