from helper import *
import random, networkx

with open("../Inputs/input_day15.txt") as f:
	program = list(map(int, f.readline().split(","))) + [0] * 10000
	program = Program(program)

	# Current coordinates, possible moves, explore order
	graph = networkx.Graph()
	coordinates = np.array([0, 0])
	moves = {
		1 : np.array([0, 1]), 
		2 : np.array([0, -1]), 
		3 : np.array([-1, 0]), 
		4 : np.array([1, 0])}
	orders = {
		1 : [1, 3, 4, 2], 
		2 : [2, 3, 4, 1], 
		3 : [3, 1, 2, 4], 
		4 : [4, 1, 2, 3]}
	# Visited with next direction, unexplored
	visited = {(0, 0) : orders[1].copy()}
	incomplete = {(0, 0)}
	result = (-1, -1)
	
	while len(incomplete) > 0:
		currentLocation = tuple(coordinates)
		if len(visited[currentLocation]) == 1: 
			direction = visited[currentLocation][0]
		else: 
			direction = visited[currentLocation].pop(0)
			if len(visited[currentLocation]) == 1: 
				incomplete.remove(currentLocation)

		output = program.runprogram([direction])
		
		if output == 0: continue
		nextLocation = tuple(coordinates + moves[direction])
		if output == 1 or output == 2:
			graph.add_edge(currentLocation, nextLocation)
		if output == 2:
			result = nextLocation
		if not nextLocation in visited:
			visited[nextLocation] = orders[direction].copy()
			incomplete.add(nextLocation)
		coordinates += moves[direction]
	
	# Feedback of the grid
	mapping = {0 : ' ', 1 : 'W', 2 : 'S', 3 : 'D'}
	drawGrid2(pointsToGrid(visited.keys()), mapping)

	# https://networkx.github.io/documentation/stable/reference/algorithms/shortest_paths.html
	print('part 1', networkx.shortest_path_length(graph, (0, 0), result))
	print('part 2', max(networkx.single_source_shortest_path_length(graph, result).values()))
