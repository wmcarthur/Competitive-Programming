line = input().split()
start = int(line[0])
target = int(line[1])


def primeFactors(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    for i in range(3,int(n**0.5)+1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i 
    if n > 2:
        factors.append(n)

    return factors

nFactors = primeFactors(start)
nLen = len(nFactors)
mFactors = primeFactors(target)
mLen = len(mFactors)

# print(nFactors)
# print(mFactors)

# Loop through nFactors
valid = True
prevInt = 0
remaining = mLen
for i in range(nLen):
    currentFactor = nFactors[i]
    # find val in mFactors 
    for j in range(prevInt, mLen):
        if mFactors[j] == currentFactor:
            mFactors[j] = 1
            prevInt = j
            remaining -= 1
            break
    else:
        valid = False
    
    if not valid:
        break
validNums = [1, 2, 3]
if valid:
    for i in range(mLen):
        if mFactors[i] not in validNums:
            valid = False
            break

# print(nFactors)
# print(mFactors)

if valid:
    print(remaining)
else:
    print(-1)



# nDict = {}
# mDict = {}

# for i in range(max(nLen, mLen)):
#     if i <= nLen:
#         if nFactors[i] in nDict:
#             nDict[nFactors[i]] += 1
#         else:
#             nDict[nFactors[i]] = 1
#     if i <= mLen:
#         if mFactors[i] in mDict:
#             mDict[mFactors[i]] += 1
#         else:
#             mDict[mFactors[i]] = 1

# nFs = [(x,y) for x in nDict.keys() for y in nDict.values()]
# mFs = [x for x in mDict.keys()]

# print(nFs)
# print(mDict)


    





# # num = start


# # counter = 0
# # while num < target:
# #     if (target - num) % 2 == 0:
# #         num *= 3
# #         counter += 1
# #     else:
# #         num *= 2
# #         counter += 1
# # if num == target:
# #     print(counter)
# # else:
# #     print(-1)
