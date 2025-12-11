def calc_area(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

data = []
points = []
with open('data', 'r') as data:
    points = [tuple(map(int, point.split(','))) for point in data.readlines()]

vertical = []
horizontal = []
n = len(points)
max_val = 0
for i in range(n-1):
    if points[i][0] == points[i+1][0]:
        horizontal.append((points[i][0], min(points[i][1], points[i+1][1]), max(points[i][1], points[i+1][1])))
    else:
        vertical.append((points[i][1], min(points[i][0], points[i+1][0]), max(points[i][0], points[i+1][0])))

sizes = []
for idx1 in range(n):
    for idx2 in range(idx1+1, n):
        val = calc_area(points[idx1], points[idx2])
        sizes.append((val, idx1, idx2))
areas = sorted(sizes, key=lambda x: x[0], reverse=True)

for area in areas:
    size, idx1, idx2 = area
    left = min(points[idx1][1], points[idx2][1])
    right = max(points[idx1][1], points[idx2][1])
    top = min(points[idx1][0], points[idx2][0])
    bottom = max(points[idx1][0], points[idx2][0])
    valid = True

    for line in vertical:
        col, upper, lower = line
        if not valid: break
        #           Correct col                       upper is in box                   lower is in box                    constrained in box                Goes through box
        if (col > left and col < right) and ((upper < top and upper > bottom) or (lower > bottom and lower < top) or (lower >= bottom and upper <= top) or (upper > top and lower < bottom)):
            valid = False

    if not valid: continue

    for line in horizontal:
        row, l, r = line
        if not valid: break
        #           Correct row                       l is in box               r is in box              constrained in box              Goes through box
        if (row < bottom and row > top) and ((l > left and l < right) or (r > left and r < right) or (l >= left and r <= right) or (l < left and r > right)):
            valid = False
    
    if valid:
        print("Largest valid area:", area[0])
        break