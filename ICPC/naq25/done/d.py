r,c = map(int, input().split())
istart, jstart = map(int, input().split())
iend, jend = map(int, input().split())
loc = (istart-1, jstart-1)
end = (iend-1, jend-1)
d = (0, 1)

def turn_left(dir):
    if dir == (0,1):
        return -1, 0
    elif dir == (-1,0):
        return 0, -1
    elif dir == (0,-1):
        return 1, 0
    elif dir == (1, 0):
        return 0, 1
def turn_right(dir):
    if dir == (0,1):
        return 1, 0
    elif dir == (1,0):
        return 0, -1
    elif dir == (0,-1):
        return -1, 0
    elif dir == (-1, 0):
        return 0, 1
def move(tup):
    return (loc[0] + tup[0], loc[1] + tup[1])

def validate(l, tup):
    newLoc = (l[0] + tup[0], l[1] + tup[1])
    if newLoc[0] < 0 or newLoc[0] >= r or newLoc[1] < 0 or newLoc[1] >= c:
        return False
    if maze[newLoc[0]][newLoc[1]] == '1':
        return False
    return True

maze = []
for _ in range(r):
    maze.append(list(input()))
# print(maze)
if maze[loc[0]][loc[1]] == '1':
    print(0)
else:
    visited = set()
    found = False
    while True:
        state = (loc, d)
        # print('loc',loc)
        # Exit condition
        if state in visited:
            break
        elif loc == end:
            found = True
            break
        visited.add(state)

        # Algo
        left = turn_left(d)
        if validate(loc, left):
            loc = move(left)
            d = left
        elif validate(loc, d):
            loc = move(d)
        else:
            d = turn_right(d)
    if found:
        print(1)
    else:
        print(0)