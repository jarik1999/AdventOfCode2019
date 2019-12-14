from helper import *
from itertools import permutations

with open("../inputs/input_day9.txt") as f:
	program = list(map(int, f.readline().split(","))) + [0] * 10000
	Program(program.copy()).runprogram([1], keepRunning = True)
	Program(program.copy()).runprogram([2], keepRunning = True)
	