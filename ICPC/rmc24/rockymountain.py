N = int(input())
sites = []

for i in range(N):
    site = input().split()
    sites.append((int(site[0]),int(site[1])))

peak = sites[0]
peakIDX = 0

# Find max
for i in range(N):
    if (sites[i][1] > peak[1]):
        peak = sites[i]
        peakIDX = i

lSite = sites[0]
initialSite = True
# Find left site
# for i in range(0,peakIDX):
#     if (sites[i][1] < lSite[1] or initialSite):
#         validPeak = True
#         m = (peak[1] - sites[i][1]) / (peak[0] - sites[i][0])
#         b = peak[1] - m * peak[0]
#         for j in range(i+1,peakIDX):
#             if (sites[j][1] > (m * sites[j][0] + b)):
#                 validPeak = False
#                 break
#         if validPeak == True:
#             if initialSite:
#                 lSite = sites[i]
#                 initialSite = False
#             elif (sites[i][1] < lSite[1]):
#                 lSite = sites[i]

for i in range(peakIDX, -1, -1):
    if (sites[i][1] < lSite[1] or initialSite):
        validPeak = True
        m = (peak[1] - sites[i][1]) / (peak[0] - sites[i][0])
        b = peak[1] - m * peak[0]
        for j in range(i+1,peakIDX):
            if (sites[j][1] > (m * sites[j][0] + b)):
                validPeak = False
                break
        if validPeak == True:
            if initialSite:
                lSite = sites[i]
                initialSite = False
            elif (sites[i][1] < lSite[1]):
                lSite = sites[i]
    
initialSite = True
rSite = sites[peakIDX+1]
# Find right site
for i in range(peakIDX+1, N):
    if (sites[i][1] <= rSite[1] or initialSite):
        validRPeak = True
        m = (sites[i][1] - peak[1]) / (sites[i][0] - peak[0])
        b = sites[i][1] - m * sites[i][0]
        for j in range(peakIDX+1, i):
            if (sites[j][1] > ((m * sites[j][0]) + b)):
                validRPeak = False
                break
        if validRPeak:
            if initialSite:
                rSite = sites[i]
                initialSite = False
            elif (sites[i][1] <= rSite[1]):
                rSite = sites[i]

print(lSite[0], lSite[1])
print(rSite[0], rSite[1])
