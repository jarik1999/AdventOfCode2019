from itertools import permutations

class Program:
	operationSize = [-1, 4, 4, 2, 2, 3, 3, 4, 4]
	def __init__(self, program):
		self.pc = 0
		self.program = program

	def getValue(self, parameter, mode = 0):
		if mode == 0: return self.program[parameter]
		elif mode == 1: return parameter

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

			if   operation == 1: self.program[c] = self.getValue(a, mode[0]) + self.getValue(b, mode[1])
			elif operation == 2: self.program[c] = self.getValue(a, mode[0]) * self.getValue(b, mode[1])
			elif operation == 3: 
				self.program[a] = inputs[inputIndex]
				inputIndex += 1
			elif operation == 4: 
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

			self.pc += self.operationSize[operation]
		raise ValueError("program ended")

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