i, com = 0, list(map(int, open("../inputs/input_day2.txt").readline().strip().split(",")))
com[1], com[2] = 12, 2
while com[i] != 99:
	command, a, b, c= com[i:i+4]
	com[c] = com[a] + com[b] if command == 1 else com[a] * com[b]
	i += 4
print(com[0])