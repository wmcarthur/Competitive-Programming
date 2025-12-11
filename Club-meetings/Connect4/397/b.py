s = list(input())
even = 0
count = 0
for c in s:
    if even == 1:
        if c == 'i':
            count += 1
        else:
            even = 0
    else:
        if c == 'o':
            count += 1
        else:
            even = 1
if (len(s) + count) % 2 == 1:
    count += 1
print(count)
