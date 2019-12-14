reactions = []
def solve(have, needed):
	if len(needed) == 1 and "ORE" in needed: return needed["ORE"]

	required = {}
	for item in needed.items():
		comp, cnt = item
		if comp == "ORE": 
			if not comp in required: required[comp] = 0
			required[comp] += cnt
			continue
		if comp in have: 
			cnt = needed[comp] - have[comp]
			have[comp] = 0
		if cnt <= 0: continue
		for reaction in reactions:
			if comp in reaction[1]:
				total = cnt // reaction[1][comp]
				if cnt % reaction[1][comp] != 0: total += 1
				if not comp in have: have[comp] = 0
				have[comp] += (total * reaction[1][comp]) - cnt
				for item2 in reaction[0].items():
					a, b = item2
					if not a in required: required[a] = 0
					required[a] += b * total
	return solve(have, required)

def possible(fuelReaction, amount):
	check = fuelReaction.copy()
	for key in check: check[key] *= amount
	ore = solve({}, check)
	return ore <= 1000000000000

with open("../Inputs/input_day14.txt") as f:
	for line in f:
		line = line.strip().split(" => ")
		left, right = line[0], line[1]
		left, right = left.split(", "), right.split(", ")
		compLeft = {}
		compRight = {}
		for comp in left:
			a, b = comp.split(" ")
			compLeft[b] = int(a)
		for comp in right:
			a, b = comp.split(" ")
			compRight[b] = int(a)
		reactions.append([compLeft, compRight])
	fuelReaction = -1
	for reaction in reactions:
		if "FUEL" in reaction[1]: fuelReaction = reaction[0]
	print('part1', solve({}, fuelReaction))
	lower, upper = 0, 1000000000000
	while lower + 1 < upper:
		middle = (lower + upper) // 2
		if possible(fuelReaction, middle): lower = middle
		else: upper = middle - 1
	if possible(fuelReaction, lower): upper = lower
	print('part2', upper)
