from helper import *

width, height = -1, -1
def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang

def distance(x, y, x2, y2): return abs(x2 - x) + abs(y2 - y)

def visible(x, y, asteroids):
	result = asteroids.copy()
	result.remove((x, y))
	for x2, y2 in asteroids:
		if x2 == x and y2 == y: continue
		deltaX, deltaY = x2 - x, y2 - y
		gcd = math.gcd(deltaX, deltaY) 
		deltaX, deltaY = deltaX // gcd, deltaY // gcd

		startX, startY = x2 + deltaX, y2 + deltaY
		while 0 <= startX < width and 0 <= startY < height:
			if (startX, startY) in result: result.remove((startX, startY))
			startX += deltaX
			startY += deltaY
	return len(result) 

with open("../inputs/input_day10.txt") as f:
	data = []
	for line in f: data.append(line.strip())
	width, height = len(data[0]), len(data)

	locations = set()
	for i in range(len(data)):
		for j in range(len(data[i])):
			if data[i][j] == '#':
				locations.add((j, i))

	maxVisible, maxVisLocation = 0, -1
	for x, y in locations:
		vis = visible(x, y, locations)
		if vis > maxVisible:
			maxVisible = vis
			maxVisLocation = (x, y)
	print('part 1', maxVisible)
	
	best, bestXY, asteroid, angles = 10 ** 9, -1, 0, []
	x, y = maxVisLocation
	for x2, y2 in locations: angles.append((getAngle([x, -100], [x, y], [x2, y2]), distance(x, y, x2, y2), (x2, y2)))
	angles.sort()

	lastAngle, res, killed = 0, 0, 0
	while len(angles) > 0:
		nextAngles, prev = [], None
		for angle, dist, loc in angles:
			if prev != None and angle == prev: nextAngles.append((angle, dist, loc))
			else:
				prev, lastAngle, killed = angle, angle, killed + 1
				if killed == 200: print('part 2', 100 * loc[0] + loc[1])
			angles = nextAngles.copy()