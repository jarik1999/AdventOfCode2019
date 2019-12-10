from itertools import permutations

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

	def runprogram(self, inputs):
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
			elif operation == 4: print(self.getValue(a, mode[0]))
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

with open("../inputs/input_day9.txt") as f:
	program = list(map(int, f.readline().split(","))) + [0] * 10000
	Program(program).runprogram([1])
	