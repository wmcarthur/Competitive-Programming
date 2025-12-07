import sys
sys.setrecursionlimit(50000)

total_beams = 0
total_splits = 0
grid = []
seen = set()

def beam(r, c):
    global total_beams
    global grid
    global seen
    global total_splits

    counted = False
    for i in range(r, len(grid)):
        # print(r, c)
        symbol = grid[i][c]
        if (i,c) in seen:
            return
        if symbol == '.':
            if not counted and (i, c) not in seen:
                total_beams += 1
                counted = True
            grid[i][c] = '|'
        elif symbol == '|':
            if counted:
                total_beams -= 1
                return
        elif symbol == '^':
            if counted:
                total_splits += 1
            if c <= 0:
                beam(i, c-1)
            if c >= len(grid[0]) - 1:
                beam(i, c+1)
            seen.add((i,c))
            return 
        seen.add((i,c))
    return 0
        
while True:
    try: line = list(input())
    except: break
    
    grid.append(line)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            beam(i,j)
            break
for row in grid:
    print(row)


print(total_beams)
print(total_splits)
