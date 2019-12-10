def cost(fuel): return 0 if (fuel // 3 - 2) <= 0 else fuel // 3 - 2 + cost(fuel // 3 - 2) 
print(sum([cost(int(line.strip())) for line in open("../inputs/input_day1.txt")]))