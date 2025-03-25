t = int(input())
def solve():
    x,y = map(int,input().split())
    if x == y:
        return -1
    
    l = max(x,y)
    # r = min(x,y)
    # v=0
    t = 1
    t = t<<40
    # lb = []
    # rb = []

    # for i in range(l.bit_length()):
    #     if l&t == 0: lb = [0] + lb
    #     else: lb = [1] + lb
    #     if r&t == 0: rb = [0] + rb
    #     else: rb = [1] + rb
    #     t*=2
    #     print(t)
    # print(*lb)
    # print(*rb)
    # n = len(lb)
    # t=1
    # #Loop through arrays of bits and find k to satisfy conditions
    # for i in range(n-1, -1, -1):
    #     if lb[i] == 1 and rb[i] == 1:
    #         pass
    return (t-l)
    


for _ in range(t):
    print(solve())