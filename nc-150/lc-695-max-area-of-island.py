from typing import List
from collections import deque
class Solution:
    visited = set()

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in self.visited:
                    c = self.get_island_size((i,j), grid) 
                    if c > ans:
                        ans = c
        return ans
    
    def get_island_size(self, start, grid) -> int:
        q = deque()
        q.append(start)
        self.visited.add(start)
        island_size = 1
        while q:
            cx, cy = q.popleft()
            for val in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = val
                if nx+cx >= 0 and nx+cx < len(grid) and ny+cy >= 0 and ny + cy < len(grid[0]) and grid[nx+cx][ny+cy] == 1 and (nx+cx, ny+cy) not in self.visited:
                    q.append((nx+cx, ny+cy))
                    self.visited.add((nx+cx, ny+cy))
                    island_size += 1
        return island_size
# grid = [
#     [1,1,0,1,1],
#     [1,0,0,0,0],
#     [0,0,0,0,1],
#     [1,1,0,1,1],
# ]
#
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(Solution().maxAreaOfIsland(grid))
