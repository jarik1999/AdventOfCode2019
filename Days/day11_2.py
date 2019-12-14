from helper import *

with open("../inputs/input_day11.txt") as f:
	program = list(map(int, f.readline().split(","))) + [0] * 10000
	program = Program(program)

	black, white = set(), set()
	white.add((0, 0))
	x, y, direction = 0, 0, 0

	try:
		while True:
			inputs = [(x, y) in white]
			color = program.runprogram(inputs)
			if color == 0:
				if (x, y) in white: white.remove((x, y))
				black.add((x, y))
			else:
				if (x, y) in black: black.remove((x, y))
				white.add((x, y))

			turn = program.runprogram([]) 
			if turn == 0: direction += 1
			else: direction -= 1
			direction %= 4

			x += directions[direction][0]
			y += directions[direction][1]
	except:
		xValues, yValues = [x for x, y in white], [y for x, y in white]
		minX, maxX, minY, maxY = min(xValues), max(xValues), min(yValues), max(yValues)
		width, height = maxX - minX + 1, maxY - minY + 1
		
		grid = zeroArray(width, height)
		for x, y in white: grid[height - 1 - y + minY][x - minX] = "X"
		replaceGrid(grid, [0], " ")
		drawGrid(grid)