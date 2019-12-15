import math, re
from itertools import *
import numpy as np

# Possible extensions
# day07 	runs series of programs once
# day07_2 	runs series of programs multiple times


# IntCode program
class Program:
	operationSize = [-1, 4, 4, 2, 2, 3, 3, 4, 4, 2]
	def __init__(self, program):
		self.pc = 0
		self.program = program
		self.base = 0

	def getValue(self, parameter, mode = 0):
		if mode == 0: return self.program[parameter]
		elif mode == 1: return parameter
		elif mode == 2: return self.program[parameter + self.base]

	def getOpModes(self, instruction):
		operation, instruction = int(instruction[-2:]), "0000" + instruction
		modes = [0] * (self.operationSize[operation] - 1)
		for i in range(len(modes)): modes[i] = int(instruction[-3 - i])
		return operation, modes

	def runprogram(self, inputs, keepRunning = False):
		inputIndex = 0
		while self.program[self.pc] != 99:
			operation, mode = self.getOpModes(str(self.program[self.pc]))

			a, b, c = self.program[self.pc + 1], self.program[self.pc + 2], self.program[self.pc + 3]
			if len(mode) >= 3 and mode[2] == 2: c += self.base # find better solution for the future

			if   operation == 1: self.program[c] = self.getValue(a, mode[0]) + self.getValue(b, mode[1])	
			elif operation == 2: self.program[c] = self.getValue(a, mode[0]) * self.getValue(b, mode[1])
				
			elif operation == 3: 
				if mode[0] == 0: self.program[a] = inputs[inputIndex]
				elif mode[0] == 2: self.program[a + self.base] = inputs[inputIndex]
				inputIndex += 1
			elif operation == 4: 
				if keepRunning:
					print(self.getValue(a, mode[0]))
				else:
					self.pc += self.operationSize[operation]
					return self.getValue(a, mode[0])
			elif operation == 5 and self.getValue(a, mode[0]) != 0:
				self.pc = self.getValue(b, mode[1])
				continue
			elif operation == 6 and self.getValue(a, mode[0]) == 0:
				self.pc = self.getValue(b, mode[1])
				continue
			elif operation == 7: self.program[c] = self.getValue(a, mode[0]) < self.getValue(b, mode[1])
			elif operation == 8: self.program[c] = self.getValue(a, mode[0]) == self.getValue(b, mode[1])
			elif operation == 9: self.base += self.getValue(a, mode[0])

			self.pc += self.operationSize[operation]
		if not keepRunning: raise ValueError()

# Java compare
def compare(a, b):
	if a > b: return 1
	elif a == b: return 0
	return -1

# Math
def gcd(a, b): return a if b == 0 else gcd(b, a % b)
def lcm(a, b): return a * b / gcd(a, b)

# Useful variables
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

# Drawing
def drawGrid(grid):
	for row in grid:
		print("".join(row))

def drawGrid2(grid, mapping):
	for row in grid:
		res = ""
		for value in row: res += mapping[value]
		print(res)

def drawColorGrid(grid, include, FILL = "X", EMPTY = " "):
	for row in grid:
		result = ""
		for value in row:
			if value in include:
				result += FILL
			else:
				result += EMPTY
		print(result)

def drawLine(line, width):
	if len(line) % width != 0: raise Exception("invalid rectangle grid")
	i = 0
	while i < len(line):
		print(line[i:i+width])
		i += width


# Grid transformations		
def pointsToGrid(points):
	xValues, yValues = [x for x, _ in points], [y for _, y in points]
	minX, maxX, minY, maxY = min(xValues), max(xValues), min(yValues), max(yValues)
	width, height = maxX - minX + 1, maxY - minY + 1
	grid = np.zeros((height, width))
	for x, y in points: grid[y - minY, x - minX] = 1
	return grid

def createGrid(line, width):
	if len(line) % width != 0: raise Exception("invalid rectangle grid")
	grid = []
	for i in range(len(line) // width):
		grid.append(line[i*width:(i+1)*width])
	return grid

def replaceGrid(grid, replace, value):
	for row in grid:
		for i in range(len(row)):
			if row[i] in replace:
				row[i] = value
	return grid

def transformGrid(grid, verticalFlip = False, horizontalFlip = False):
	if verticalFlip: grid = [row[::-1] for row in grid]
	if horizontalFlip: grid = grid[::-1]
	return grid

# Similar to zeros from numpy, but can contain any type
def zeroArray(width, height):
	return [[0 for i in range(width)] for j in range(height)]

