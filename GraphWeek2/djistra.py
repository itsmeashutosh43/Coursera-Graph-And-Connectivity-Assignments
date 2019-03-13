
from collections import defaultdict


def findMin(dist):

	minimum=min(dist.values())

	for i,j in dist.items():
		if j==minimum:
			return i

	return


def djistraAlgo(adj,source):

	Q=[]
	Visited=[]
	
	for vertex in adj:
		dist[vertex]=1000000
		Q.append(vertex)

	dist[source]=0
	diffDist=dist.copy()


	while Q:
		u=findMin(dist)
		Q.pop
		Visited.append(u)
		for neighbour in adj[u]:
			if neighbour in Visited:
				pass
			else:
				x=dist[u]+adj[u][neighbour]
				if dist[neighbour] >x:
					dist[neighbour] = x 
					diffDist[neighbour] = x

		Q.remove(u)
		dist.pop(u)

	return diffDist
		














content = open('djistra.txt', 'r').readlines()

adj=defaultdict(dict)
dist=defaultdict()

for line in content:
	preproccess=line.strip().split('\t')
	index=int(preproccess[0])
	for i in preproccess[1:]:
		noComma=i.split(',')
		adj[index][int(noComma[0])]=int(noComma[1])
		
		#adj[index].append((int(noComma[0]),int(noComma[1])))

dist=djistraAlgo(adj,1)

for a in answers:
	print(dist[a])

	

