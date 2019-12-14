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
