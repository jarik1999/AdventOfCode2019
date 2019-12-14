from helper import *

with open("../inputs/input_day8.txt") as f:
	length = 150
	layers = createGrid(f.readline(), length)
	
	result = [0] * length
	for i in range(length):
		for layer in layers:
			if layer[i] == '2': continue
			result[i] = layer[i]
			break
	result = "".join(result)
	drawLine(result.replace("0", " ").replace("1", "X").replace("2", " "), 25)