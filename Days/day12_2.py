from helper import *
import re, math

RE = re.compile("<x=(?P<x>[-0-9]+), y=(?P<y>[-0-9]+), z=(?P<z>[-0-9]+)>")
initLocations = []
with open("../inputs/input_day12.txt") as f:
	for line in f:
		match = RE.match(line.strip())
		x, y, z = int(match.group('x')), int(match.group('y')), int(match.group('z'))
		initLocations.append((x, y, z))

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