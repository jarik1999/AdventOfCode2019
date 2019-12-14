from helper import *

def runPrograms(programs, settings):
	output = 0
	for i in range(len(programs)): output = programs[i].runprogram([settings[i], output])
	return output

with open("../inputs/input_day7.txt") as f:
	program = list(map(int, f.readline().split(","))) + [0, 0, 0]
	best = 0
	for x in list(permutations(range(5))):
		programs = [Program(program.copy()) for i in range(5)]
		best = max(best, runPrograms(programs, x))
	print(best)