tot = 0

with open("Day1-input", "r") as f:
	for line in f:
		num = int(line)
		while (int(num/3)-2)>0:	
			num = int(num/3)-2
			tot += num

print(tot)
