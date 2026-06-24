class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])

        def dfs(x,y):
            if (x < 0 or x >= N or y < 0 or y >= M or grid[x][y] == 0):
                return 0
            grid[x][y] = 0
            return 1 + dfs(x+1,y) + dfs(x-1,y) + dfs(x,y+1) + dfs(x,y-1)

        max_area = 0
        for i in range(N):
            for j in range(M):
                max_area = max(max_area, dfs(i,j))
        return max_area
        
            
