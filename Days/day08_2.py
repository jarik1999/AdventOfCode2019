with open("../inputs/input_day8.txt") as f:
	data = f.readline()
	
	length = 25 * 6
	total = len(data) // length
	layers = [data[i*length:(i+1)*length] for i in range(total)]

	final = [0] * length
	for i in range(length):
		for layer in layers:
			if layer[i] == '2': continue
			final[i] = layer[i]
			break
	for i in range(6):print("".join(final[i*25:(i+1)*25]).replace("0", " ").replace("1", "X").replace("2", " "))