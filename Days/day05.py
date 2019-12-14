from helper import *

with open("../inputs/input_day5.txt") as f:
	program = list(map(int, f.readline().split(","))) + [0, 0, 0]
	Program(program.copy()).runprogram([1], True)
	Program(program.copy()).runprogram([5], True)