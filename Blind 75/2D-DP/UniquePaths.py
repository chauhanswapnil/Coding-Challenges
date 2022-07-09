class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Bottom-Up DP
        row = [1] * n
        for i in range(m-1):
            newRow = [1] * n
            for j in range(n-2,-1,-1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        return row[0]
        # DFS brute force approach Top Down approach, can be memoized
        # grid = [[0 for _ in range(n)] for _ in range(m)]
        # grid[m-1][n-1] = 1
        # def dfs(a,b):
        #     if a >= m or b>=n:
        #         return 0
        #     if grid[a][b] == 1:
        #         return 1
        #     return dfs(a+1,b) + dfs(a,b+1)
        # return dfs(0,0)
    
    
print(Solution().uniquePaths(7,3))