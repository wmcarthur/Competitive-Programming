grid = []
seen = {}

def beam(r, c):
    global grid
    global seen
    
    for i in range(r, len(grid)):
        symbol = grid[i][c]
        if (i,c) in seen:
            return seen[(i,c)]
        elif symbol == '^':
            if c > 0 and c < len(grid[0]) - 1:
                seen[(i,c)] = beam(i, c-1) + beam(i, c+1)
            elif c > 0:
                seen[(i,c)] = beam(i, c-1)
            elif c < len(grid[0]) - 1:
                seen[(i,c)] = beam(i, c+1)
            return seen[(i,c)]
    return 1

with open('data', 'r') as data:
    grid = [line.strip() for line in data.readlines()]        

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            print("Timelines:", beam(i,j))
            break