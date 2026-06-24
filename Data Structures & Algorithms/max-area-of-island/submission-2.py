class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        max_area = 0

        def dfs(i,j):
            if i < 0 or i >= N or j < 0 or j >= M or grid[i][j] == 0:
                return 0

            grid[i][j] = 0

            return 1 + dfs(i+1,j) + dfs(i,j+1) + dfs(i-1,j) + dfs(i,j-1)

        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    max_area = max(max_area,dfs(i,j))
        
        return max_area
            
