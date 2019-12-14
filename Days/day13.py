from helper import *

with open("../Inputs/input_day13.txt") as f:
	program = list(map(int, f.readline().split(","))) + [0] * 10000
	program[0] = 2
	program = Program(program)

	ballX, paddleX = -1, -1
	width, height = 42, 24
	count, score = 0, 0
	grid = np.zeros((height, width))

	try:
		while True:
			d = compare(ballX, paddleX)
			x = program.runprogram([d])
			y = program.runprogram([d])
			t = program.runprogram([d])

			if x == -1 and y == 0: score = t
			else:
				grid[y][x] = t
				if t == 2: count += 1
				elif t == 3: paddleX = x
				elif t == 4: ballX = x	
	except ValueError:
		print("part1", count)
		print("part2", score)