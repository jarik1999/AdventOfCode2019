from helper import *

with open("../Inputs/input_day16.txt") as f:
	#inp = f.readline()
	#print(len(inp))
	inp = "12345678" * 10
	num = [int(inp[i]) for i in range(len(inp))]
	num = np.array(num, dtype='int8')
	order = np.array([0, 1, 0, -1], dtype='int8')

	for i in range(4):
		print(i)
		num2 = np.zeros(len(num), dtype='int8')
		index = 0
		
		phase = 1
		for j in range(len(num)):
			result = 0
			current = 0
			currentPhase = 1
			if currentPhase == phase:
				current = (current + 1) % 4
				currentPhase = 0
			for k in range(len(num)):
				#print('index', k, 'multiply', order[current], num[k])
				result += order[current] * num[k]
				currentPhase += 1
				if currentPhase == phase:
					current = (current + 1) % 4
					currentPhase = 0
			num2[index] = abs(result) % 10
			index += 1
			#num2.append(abs(result) % 10)
			#print('resulted', abs(result) % 10)
			phase += 1
		print(num2)
		num = num2
	location = int(''.join([str(x) for x in num[:7]]))
	print('part1', num[:8])
	print('location', location)
	#print(num[location:location+8])
	#print(num[:8])
	#36739874
	#77749681
'''
from helper import *

with open("../Inputs/input_day16.txt") as f:
	inp = f.readline()

	#inp = "12345678"
	num = [int(inp[i]) for i in range(len(inp))]
	num = np.array(num, dtype='int8')
	order = np.array([0, 1, 0, -1], dtype='int8')
	phases = []
	for phase in range(1, len(num) + 1):
		print('mask', phase)
		mask = np.zeros(len(num), dtype='int8')
		currentPhase = 1
		current = 0
		for j in range(len(num)):
			if currentPhase == phase:
				current = (current + 1) % 4
				currentPhase = 0
			mask[j] = order[current]
			currentPhase += 1
		phases.append(mask)
		print(mask)

	for i in range(100):
		print(i, num)
		num2 = np.zeros(len(num), dtype='int8')
		for j in range(len(num)):
			
			num2[j] = sum(phases[j] * num)
			num2[j] = abs(num2[j]) % 10
		num = num2

	print(num)
	location = int(''.join([str(x) for x in num[:7]]))
	print(location)
	print(num[location:location+8])
	#print(num[:8])
	#36739874
	#77749681
'''