tot = 0

with open("Day1-input", "r") as f:
	for line in f:
		tot += int(int(line)/3)-2

print(tot)
