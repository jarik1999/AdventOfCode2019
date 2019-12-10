com = list(map(int, open("../inputs/input_day2.txt").readline().strip().split(",")))
for j in range(100):
	for k in range(100):
		com2 = com.copy()
		i, com2[1], com2[2] = 0, j, k
		while com2[i] != 99:
			command, a, b, c= com2[i:i+4]
			com2[c] = com2[a] + com2[b] if command == 1 else com2[a] * com2[b]
			i += 4
		if com2[0] == 19690720: print(j * 100 + k)