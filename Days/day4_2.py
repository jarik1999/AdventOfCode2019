cnt = 0
for i in range(109165, 576724):
	d, double = "-" + str(i) + "-", False
	checks = [d[j] == d[j+1] and d[j] != d[j-1] and d[j] != d[j+2] for j in range(1, len(d) - 2)]
	if sorted(str(i)) == list(str(i)) and any(checks): cnt += 1
print(cnt) 