class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        rows,cols=len(heights),len(heights[0])
        p,a=set(),set()
        def dfs(r,c,visited,prev):
            if ((r,c) in visited or r<0 or r>=rows or c<0 or c>=cols or heights[r][c]<prev):
                return
            visited.add((r,c))
            dfs(r+1,c,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])
        for r in range(rows):
            dfs(r,0,p,heights[r][0])
            dfs(r,cols-1,a,heights[r][cols-1])
        for c in range(cols):
            dfs(0,c,p,heights[0][c])
            dfs(rows-1,c,a,heights[rows-1][c])
        res=list(p&a)
        return res            
