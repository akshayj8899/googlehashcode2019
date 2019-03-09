import collections
from tqdm import tqdm


tags = collections.Counter()
data = {}

skip = 0
photo = 0
with open('B.txt') as f:
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

file = open("B.out","w")

#print(data[0])

for whatever, photo in tqdm(data.items()):
	#photo = data[photo]
	phototags = photo["tags"]
	photo["used"] = True
	#del data[int(photo["id"])]
	for partner in data:
		partner = data[partner]
		othertags = partner["tags"]
		if(len(set(phototags).intersection(othertags)) > 1 and partner["used"] == False):
			file.write(str(photo["id"]))
			file.write("\n")
			file.write(str(partner["id"]))
			file.write("\n")
			partner["used"] = True
			#del data[int(partner["id"])]
file.close() 



#print(data[0])



			
'''
D = sorted(D.items(), key=lambda D: D[1])

file = open("B.out","w")
file.write(str(int(len(D))))
file.write("\n")


newlist = []
for key, val in D:
	newlist.append(key)

for val in newlist:
	if(val > 80000):
		print("you done fucked up")


start = 0
end = len(D) - 1

for bob in range(0, int(len(D)/2)):
	file.write(str(newlist[start]))
	file.write("\n")
	file.write(str(newlist[end]))
	file.write("\n")
	start += 1
	end -= 1

for key, val in D:
	file.write(str(key))
	file.write("\n")
	start += 1
	end -= 1
file.close() 

'''