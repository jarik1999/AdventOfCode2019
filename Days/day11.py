from helper import *

with open("../inputs/input_day11.txt") as f:
	program = list(map(int, f.readline().split(","))) + [0] * 10000
	program = Program(program)
	# 0 if white, 1 if black
	black, white = set(), set()
	black.add((0, 0))
	x, y, direction = 0, 0, 0

	try:
		while True:
			if (x, y) in white: 
				inputs = [1]
				white.remove((x, y))
				black.add((x, y))
			elif (x, y) in black:
				inputs = [0]
				black.remove((x, y))
				white.add((x, y))
			else: 
				inputs = [0]
				white.add((x, y))

			color = program.runprogram(inputs)
			turn = program.runprogram([]) 

			if turn == 0: direction += 1
			else: direction -= 1
			direction %= 4

			x += directions[direction][0]
			y += directions[direction][1]
	except:
		print(len(white) + len(black))
