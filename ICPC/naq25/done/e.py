import math
r = 0
y = 0

for round in range(10):
    rline = list(map(int, input().split()))
    yline = list(map(int, input().split()))
    rn = rline[0]
    yn = yline[0]
    
    rpairs = []
    ypairs = []

    for i in range(1, len(rline), 2):
        rpairs.append(math.sqrt((rline[i]-144)**2 + (rline[i+1] - 84)**2))
    for i in range(1, len(yline), 2):
        ypairs.append(math.sqrt((yline[i]-144)**2 + (yline[i+1] - 84)**2))

    rpairs = sorted(rpairs)
    ypairs = sorted(ypairs)

    if len(rpairs) == 0:
        y += len(ypairs)
    elif len(ypairs) == 0:
        r += len(rpairs)
    else:

        if rpairs[0] < ypairs[0]:
            for val in rpairs:
                if val < ypairs[0]:
                    r += 1
                else:
                    break                
        else:
            for val in ypairs:
                if val < rpairs[0]:
                    y += 1
                else:
                    break
print(r,y)