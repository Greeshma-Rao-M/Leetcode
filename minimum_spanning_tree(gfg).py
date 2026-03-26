class Solution:
    def spanningTree(self, V, edges):
        # code here
        parent=[i for i in range(V)]
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            px,py=find(x),find(y)
            if px!=py:
                parent[px]=py
                return True
            return False
        edges.sort(key=lambda x:x[2])
        total_weight=0
        for u,v,w in edges:
            if union(u,v):
                total_weight+=w
        return total_weight
