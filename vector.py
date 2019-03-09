import collections
from tqdm import tqdm
import numpy as np
import random	
from tqdm import tqdm


tags = collections.Counter()
data = {}

vocab = []
skip = 0
with open('d_pet_pictures.txt') as f:
	for line in f:
		if(skip == 0):
			skip += 1
			pass
		else:
			if(line.split(" ")[0] == "H"):
				tags = line.replace("\n", "").split(" ")[2:]
				for tag in tags:
					vocab.append(tag)

vocab = list(set(vocab))



skip = 0
photo = 0
matrix = []
order = []
with open('d_pet_pictures.txt') as f:
	for line in f:
		if(skip == 0):
			skip += 1
			pass
		else:
			if(line.split(" ")[0] == "H"):
				vector = [0]*len(vocab)
				tags = line.replace("\n", "").split(" ")[2:]
				for tag in tags:
					vector[vocab.index(tag)] = 1
				vector = np.array(vector)
				#print(type(vector))
				matrix.append(vector)
				data[photo] = {'size': line.split(" ")[1],
				'tags':tags,
				'vector': vector,
				'id': str(photo),
				'used': False,
				'orientation': line.split(" ")[0]
				}
				order.append(photo)
			photo += 1


f = open("D.out", "w")

for x, photo in tqdm(data.items()):
	npmatrix = np.array(matrix)
	pick = data[x]
	if(pick["used"] == False):
		vector = pick["vector"]
		id = pick["id"]

		result = np.matmul(npmatrix, vector.T)
		min = np.argmin(result)
		max = np.argmax(result)
		min = result[min]
		max = result[max]

		middle = (max - min) / 2
		idx = (np.abs(result-middle)).argmin()

		photo1 = id
		photo2 = order[idx]
		
		f.write(str(photo1))
		f.write("\n")
		f.write(str(photo2))
		f.write("\n")
		
		#print(photo1, photo2)
		
		pick["used"] = True
		data[photo2]["used"] = True
		del matrix[idx]
		del order[idx]
		
		del matrix[0]
		del order[0]
		
		
f.close()
print("Done")		




print(len(data))
raise Exception



'''
print("Max:", max)
print("Min:", min)
print("Middle:", middle)
print("ID Close:", idx)
print("CLOSE:", result[idx])

print("Photo1:", id)
print("Photo2:", order[idx])
'''


'''
half = (max-min)/2
count = 0

for x in result:
	if(x == half):
		print("FOUND")
	count += 1
print(len(result))
'''