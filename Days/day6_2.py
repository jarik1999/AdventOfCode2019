g,bfs,f={},lambda s, n, d, v: d if n == s else min([bfs(s,e,d+1,n) if e != v else 10**9 for e in g[n]]+[10**9]),"../inputs/input_day6.txt"
for (a, b) in [l.strip().split(")") for l in open(f)]:g[a],g[b]=[b] if a not in g else g[a]+[b],[a] if b not in g else g[b]+[a]
print(bfs("SAN","YOU",0,"")-2) # sorry couldnt help myself