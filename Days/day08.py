from helper import *

with open("../inputs/input_day8.txt") as f:
	layers = createGrid(f.readline(), 150)
	counts = [(x.count('0'), x.count('1'), x.count('2')) for x in layers]
	print(min(counts)[1] * min(counts)[2])