with open("../Inputs/input_day16.txt") as f:
	inp = f.readline()
	num = [int(inp[i]) for i in range(len(inp))]
	num *= 10000
	location = int(''.join([str(x) for x in num[:7]]))
	print(location)
	for iteration in range(100):
		i = len(num) - 2
		while i >= location:
			num[i] = (num[i] + num[i+1]) % 10
			i -= 1
	print(num[location:location+8])