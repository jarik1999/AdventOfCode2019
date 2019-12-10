g = {}
def dfs(u, d, p = None): return d + sum([dfs(v, d+1, u) if u != v else 0 for v in g[u]])

with open("../inputs/input_day6.txt") as f:
	for line in f:
		a, b = line.strip().split(")")
		if a not in g: g[a] = set()
		if b not in g: g[b] = set()
		g[a].add(b)
print(dfs("COM", 0))