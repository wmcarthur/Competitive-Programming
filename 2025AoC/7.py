total_splits = 0
grid = []
seen = set()

def beam(r, c):
    global grid
    global seen
    global total_splits
    
    if (r, c) in seen:
        return
    
    counted = False
    for i in range(r, len(grid)):
        symbol = grid[i][c]
        if symbol == '.':
            if not counted and (i, c) not in seen:
                counted = True
            grid[i][c] = '|'
        elif symbol == '|':
            if counted:
                return
        elif symbol == '^':
            if counted:
                total_splits += 1
            if c > 0:
                beam(i, c-1)
            if c < len(grid[0]) - 1:
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
print("splits:",total_splits)