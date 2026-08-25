class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(n):
            visited.add(n)
            for nei in graph[n]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        res = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1
        return res