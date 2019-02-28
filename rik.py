file = open("me_at_the_zoo.in", "r")

eerstelijn = map(lambda x: int(x), file.readline().split(" "))

V = eerstelijn[0]
E = eerstelijn[1]
R = eerstelijn[2]
C = eerstelijn[3]
X = eerstelijn[4]


#videogroootettete
vg = map(lambda x: int(x), file.readline().split(" "))


#cache endpoint verbindings latency winst
CE = dict() # dict met (endpoint, cacheserver): (latencywinst)
EC = dict() # met endpoint: (cacheserver, latencywinst)

i = 0
while i < E:
    lijn = map(lambda x: int(x), file.readline().split(" "))
    latency = lijn[0]
    EC[i] = dict()
    for j in range(lijn[1]):
        sublijn = map(lambda x: int(x), file.readline().split(" "))
        CE[(i, sublijn[0])] = latency - sublijn[1]
        EC[i][sublijn[0]] = latency - sublijn[1]
    i += 1



print EC


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



#
caches = map(lambda _: dict(), range(C))
while i < V:
    for cache in caches:
        print " "
        
                            
        






#CE.sort(key = lambda x: -x[0])


#print(CE)
#print(CE[(5, 9)])
