with open("../inputs/input_day3.txt") as f:
	i, loc, best = 0, [set(), set()], 10**9
	for line in f:
		x, y, moves = 0, 0, 0
		for entry in line.split(","):
			for _ in range(int(entry[1:])):
				if entry[0] == 'L': x -= 1
				if entry[0] == 'R': x += 1
				if entry[0] == 'U': y += 1
				if entry[0] == 'D': y -= 1
				moves += 1
				if not (x, y) in loc[i]: loc[i].add((x, y))
		i += 1
	for location in loc[0]:
		if location in loc[1]: best = min(best, abs(location[0]) + abs(location[1])) 
	print(best)