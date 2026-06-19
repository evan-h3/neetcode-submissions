class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        visited = set()
        count = 0

        def dfs(node):
            for child in adj[node]:
                if child not in visited:
                    visited.add(child)
                    dfs(child)
        
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                count+=1
        
        return count
            