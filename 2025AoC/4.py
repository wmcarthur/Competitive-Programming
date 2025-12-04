def check_adj(r, c, rows, cols, grid):
    count = 0
    count += (r > 0 and grid[r-1][c] == '@') #up
    count += (r > 0 and c > 0 and grid[r-1][c-1] == '@') #top left
    count += (c > 0 and grid[r][c-1] == '@') #left
    count += (r > 0 and c < cols - 1 and grid[r-1][c+1] == '@') #top right
    count += (c < cols - 1 and grid[r][c+1] == '@') #right
    count += (r < rows - 1 and c < cols - 1 and grid[r+1][c+1] == '@') #bottom right
    count += (r < rows - 1 and grid[r+1][c] == '@') #bottom
    count += (r < rows - 1 and c > 0 and grid[r+1][c-1] == '@') #bottom left
    return count

g = []
while True:
    try:
        line = input().strip()
        g.append(list(line))
    except:
        break
# for row in g:
#     print(row)
rows = len(g)
cols = len(g[0])
total = 0
lastTotal = -1
while lastTotal != total:
    lastTotal = total
    # print(lastTotal, total)
    for i in range(rows):
        for j in range(cols):
            if g[i][j] != '@':
                continue
            val = check_adj(i, j, rows=rows, cols=cols, grid=g)
            if val < 4:
                total += 1
                g[i][j] = '.'
                # print(val)
                # print(i, j)
    
print(total)