from helper import *

def runPrograms(programs, settings):
	output, i, last, n = 0, 0, 0, len(programs)
	try:
		while True:
			if i < n: output = programs[i].runprogram([settings[i], output])
			else: output = programs[i % n].runprogram([output])

			if i % n == n - 1: last = max(last, output)
			i += 1
	except ValueError: return last

with open("../inputs/input_day7.txt") as f:
	program = list(map(int, f.readline().split(","))) + [0, 0, 0]
	best = 0
	for x in list(permutations(range(5, 10))):
		programs = [Program(program.copy()) for i in range(5)]
		best = max(best, runPrograms(programs, x))
	print(best)