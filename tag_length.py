import collections

tags = collections.Counter()
data = {}

skip = 0
photo = 0
with open('E.txt') as f:
	for line in f:
		if(skip == 0):
			skip += 1
			pass
		else:
			if(line.split(" ")[0] == "H"):
				tags = line.replace("\n", "").split(" ")[2:]
				data[photo] = {'size': line.split(" ")[1],
				'tags':tags,
				'id': str(photo),
				'used': False
				}
			photo += 1

file = open("E.out","w")


data = sorted(data.items(), key=lambda data: data[1])

file = open("D.out","w") 
file.write(str(int(len(D))))
file.write("\n")
for key, val in D:
	file.write(str(key))
	file.write("\n")
file.close() 

