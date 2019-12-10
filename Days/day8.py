with open("../inputs/input_day8.txt") as f:
	data = f.readline()
	
	length = 25 * 6
	total = len(data) // length
	layers = [data[i*length:(i+1)*length] for i in range(total)]

	counts = [(x.count('0'), x.count('1'), x.count('2')) for x in layers]
	print(min(counts)[1] * min(counts)[2])