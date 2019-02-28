file = open("kittens.in", "r")





"""
#credit http://obogason.com/sorting-algorithms-in-python/
def insertion_sort(m, sort_by=(lambda a, b: a < b)):
	def insert_item(m, item0):
		for i, item in enumerate(m):
			if sort_by(item0, item):
				m.insert(i, item0)
				return
		m.append(item0)

	if len(l) <= 1:
		return l

	sorted_list = []
	for item in l:
		insert_item(sorted_list, item)
	return sorted_list

"""


#STAP 1
#PER VIDEO PER CACHE DE TIJDSWINST * opvragen / gehuegen

#STAP 2
#SORT

#STEP 3
#START MET VULLEN



eerstelijn = map(lambda x: int(x), file.readline().split(" "))

V = eerstelijn[0]
E = eerstelijn[1]
R = eerstelijn[2]
C = eerstelijn[3]
X = eerstelijn[4]


#videogroootettete
VG = map(lambda x: int(x), file.readline().split(" "))


#cache endpoency winst
CE = dict() # dict met cacheserver: dict(): endpoint - > latencywinst)
EC = dict() # met endpoint: (dict(): cacheserver -> latencywinst)

i = 0
while i < E:
    lijn = map(lambda x: int(x), file.readline().split(" "))
    latency = lijn[0]
    EC[i] = dict()
    for j in range(lijn[1]):
        sublijn = map(lambda x: int(x), file.readline().split(" "))
        if sublijn[0] not in CE:
            CE[sublijn[0]] = dict()
        CE[sublijn[0]][i] = latency - sublijn[1]
        EC[i][sublijn[0]] = latency - sublijn[1]
        
    i += 1




#array met video: (dict: endpoint -> aantal requests)
video = map(lambda _: dict(), range(V))
i = 0
while i < R:
    lijn = map(lambda x: int(x), file.readline().split(" "))
    if lijn[1] in video[lijn[0]]:
        video[lijn[0]][lijn[1]] += lijn[2]
    else:
        video[lijn[0]][lijn[1]] = lijn[2]
    i += 1


file.close()




#print video
#print " "



#VIDEO CACHE: dict: (video, cache) -> efficientie

VC = dict()
i = 0
while i < V:
    for endpoint in video[i]:
        for cache in EC[endpoint]:
            if (i, cache) in VC:
                VC[(i, cache)] += EC[endpoint][cache] * video[i][endpoint] / VG[i]
            else:
                VC[(i, cache)] = EC[endpoint][cache] * video[i][endpoint] / VG[i]
    i += 1




sortedd = map(lambda x: [x, VC[x]], sorted(VC, key=VC.get, reverse=True))

#print sortedd
#print video[99]

#ARRAY MET LISTS MET VIDEOS
CACHES = map(lambda _: [X, []], range(C))

while len(sortedd) > 0:
    curr = sortedd.pop(0)
    vidcache = curr[0]
    if VG[vidcache[0]] <= CACHES[vidcache[1]][0]:
        CACHES[vidcache[1]][1].append(vidcache[0])
        CACHES[vidcache[1]][0] -= VG[vidcache[0]]
        for vidcacheeff2 in sortedd:
            vidcache2 = vidcacheeff2[0]
            if vidcache2[0] == vidcache[0] and vidcache[1] != vidcache2[1]:
                penalty = 0
                for endpoint in CE[vidcache[1]]:
                    """print "endpoint", endpoint
                    print vidcache
                    print vidcache2
                    print EC[endpoint]
                    print video[vidcache[0]]
                    print "endpoint", endpoint"""
                    if vidcache2[1] in EC[endpoint] and vidcache[0] not in CACHES[vidcache[1]] and endpoint in video[vidcache[0]]:
                        #print video[vidcache[0]][endpoint]
                        penalty += CE[vidcache[1]][endpoint] * video[vidcache[0]][endpoint] / VG[vidcache[0]]
                sortedd[vidcache2[1]][1] -= penalty
        #print sortedd
        sortedd = sorted(sortedd, key=lambda x: x[0][0], reverse=True)





newfile = open("output.out", "w")
newfile.write(str(C) + "\n")
i = 0
for cache in CACHES:
    newfile.write(str(i))
    for video in cache[1]:
        newfile.write(" " + str(video))
    newfile.write("\n")
    i += 1

newfile.close()




#CE.sort(key = lambda x: -x[0])


#print(CE)
#print(CE[(5, 9)])







