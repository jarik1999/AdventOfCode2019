from helper import *

with open("../inputs/input_day8.txt") as f:
	height, width, length = 6, 25, 150
	layers, result = createGrid(f.readline(), length), np.zeros(length)
	for i in range(length):
		for layer in layers:
			if layer[i] == '2': continue
			result[i] = int(layer[i])
			break
	drawColorGrid(result.reshape(6, 25),[1])