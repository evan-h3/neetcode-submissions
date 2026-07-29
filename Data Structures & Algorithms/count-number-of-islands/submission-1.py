class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        N = len(grid)
        M = len(grid[0])

        def dfs(i,j):
            if i < 0 or i >= N or j < 0 or j >= M or grid[i][j] != '1':
                return
            grid[i][j] = '#' #if we want to reverse changes
            
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        count = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == '1':
                    count+=1
                    dfs(i,j)
        
        # reverse the changes we made
        # for i in range(N):
        #   for j in range(M):
        #       if grid[i][j] == "#":
        #           grid[i][j] = "1"

        return count
