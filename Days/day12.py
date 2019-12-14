from helper import *

positions = np.array([[10, 15, 7], [15, 10, 0], [20, 12, 3], [0, -3, 13]])
velocities = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]])
prev = set()

for _ in range(1000):
	for j, k in permutations(range(4), 2):
		for x in range(3): 
			velocities[j][x] += compare(positions[k][x], positions[j][x])
	positions += velocities

result = 0
for i in range(4): result += sum(map(abs, positions[i])) * sum(map(abs, velocities[i]))
print(result)