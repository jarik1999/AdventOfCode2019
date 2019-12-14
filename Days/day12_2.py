from helper import *

initLocations = [[10, 15, 7], [15, 10, 0], [20, 12, 3], [0, -3, 13]]
result, prev = 1, set()
for i in range(3):
	loc, v, step = [initLocations[j][i] for j in range(4)], [0] * 4, 0
	while True:
		for j in range(4):
			for k in range(4): 
				v[j] += compare(loc[k], loc[j])
		for j in range(4): 
			loc[j] += v[j]
		if tuple(loc + v) in prev: 
			prev = set()
			result = lcm(result, step)
			break
		prev.add(tuple(loc + v))
		step += 1
print(result) 