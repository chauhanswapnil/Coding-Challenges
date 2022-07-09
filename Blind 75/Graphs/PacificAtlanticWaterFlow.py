class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # We know that the edge rows and columns can reach the pacific or atlantic
        # ocean so we start from there and see if we can keep going inside using dfs
        # We keep a visited to know if we have visited that cell before.
        
        ROWS, COLS = len(heights), len(heights[0])
        
        pac, atl = set(), set()
        
        def dfs(r,c,visited,prevHeight):
            if ((r,c) in visited or 
                r<0 or c<0 or 
                r==ROWS or c==COLS or 
                heights[r][c]<prevHeight):
                return
            visited.add((r,c))
            dfs(r+1,c,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])
        
        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS - 1,c,atl,heights[ROWS-1][c])
        
        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLS-1, atl, heights[r][COLS-1])
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res
    