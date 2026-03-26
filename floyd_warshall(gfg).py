class Solution:
	def floydWarshall(self, dist):
		#Code here
		V=len(dist)
		INF=10**8
		for i in range(V):
		    for j in range(V):
		        if dist[i][j]==INF:
		            dist[i][j]=float('inf')
		for via in range(V):
		    for i in range(V):
		        for j in range(V):
		            if dist[i][via]!=float('inf') and dist[via][j]!=float('inf'):
		                if dist[i][via]+dist[via][j]<dist[i][j]:
		                    dist[i][j]=dist[i][via]+dist[via][j]
		for i in range(V):
		    for j in range(V):
		        if dist[i][j]==float('inf'):
		            dist[i][j]=INF
		            
