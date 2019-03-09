import collections


tags = collections.Counter()
paired = {}

skip = 0
photo = 0
counter = 0

with open('B.txt') as f:
	for line in f:
		if(skip == 0):
			skip += 1
			pass
		else:
			if(line.startswith("V")):
				if(photo % 2 == 0):				
					paired[counter] = {'photo1': photo,
										'photo2': photo+1,
										'tags': len(line.replace("\n", "").split(" ")[2:])
					}
					counter += 1
				if(photo % 2 == 1):
					paired[counter - 1]["tags"] += len(line.replace("\n", "").split(" ")[2:])
			photo += 1

print(paired)


#print(paired[0])

paired = sorted(paired.items(), key=lambda x: x[1]["tags"])

file = open("B.out","w") 
file.write(str(int(len(paired)/2)))
file.write("\n")
for key, val in paired:
	file.write(str(val["photo1"]) + " " + str(val["photo2"]))	
	file.write("\n")
file.close()

