from typing import List


class Solution:

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        adj=[[] for i in range(V)]
        for u,v,w in edges:
            adj[u].append((v,w))
        visited=[False]*V
        st=[]
        def dfs(node):
            visited[node]=True
            for nei,wt in adj[node]:
                if not visited[nei]:
                    dfs(nei)
            st.append(node)
        for i in range(V):
            if not visited[i]:
                dfs(i)
        dist=[float('inf')]*V
        dist[0]=0
        while st:
            node=st.pop()
            if dist[node]!=float('inf'):
                for nei,wt in adj[node]:
                    if dist[node]+wt<dist[nei]:
                        dist[nei]=dist[node]+wt
        for i in range(V):
            if dist[i]==float('inf'):
                dist[i]=-1
        return dist
