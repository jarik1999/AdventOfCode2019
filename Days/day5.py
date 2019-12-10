program, operationSize = [], [-1, 4, 4, 2, 2, 3, 3, 4, 4]

def getValue(parameter, mode = 0):
	if mode == 0: return program[parameter]
	elif mode == 1: return parameter

def getOpModes(instruction):
	operation, instruction = int(instruction[-2:]), "0000" + instruction
	modes = [0] * (operationSize[operation] - 1)
	for i in range(len(modes)): modes[i] = int(instruction[-3 - i])
	return operation, modes

def runProgram():
	pc = 0
	while program[pc] != 99:
		operation, mode = getOpModes(str(program[pc]))
		a, b, c = program[pc + 1], program[pc + 2], program[pc + 3]

		if   operation == 1: program[c] = getValue(a, mode[0]) + getValue(b, mode[1])
		elif operation == 2: program[c] = getValue(a, mode[0]) * getValue(b, mode[1])
		elif operation == 3: program[a] = int(input('input required: \n'))
		elif operation == 4: print(getValue(a, mode[0]))
		elif operation == 5 and getValue(a, mode[0]) != 0:
			pc = getValue(b, mode[1])
			continue
		elif operation == 6 and getValue(a, mode[0]) == 0:
			pc = getValue(b, mode[1])
			continue
		elif operation == 7: program[c] = getValue(a, mode[0]) < getValue(b, mode[1])
		elif operation == 8: program[c] = getValue(a, mode[0]) == getValue(b, mode[1])

		pc += operationSize[operation]

with open("../inputs/input_day5.txt") as f:
	program = list(map(int, f.readline().split(","))) + [0, 0, 0]
	runProgram()