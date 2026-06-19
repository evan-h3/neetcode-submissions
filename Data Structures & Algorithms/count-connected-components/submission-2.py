class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        visited = set()
        count = 1
        print(graph)
        def dfs(val):
            if val in visited:
                return
            visited.add(val)
            for nei in graph[val]:
                dfs(nei)

        for node in graph:
            if node not in visited:
                dfs(node)
                count += 1
        
        return count