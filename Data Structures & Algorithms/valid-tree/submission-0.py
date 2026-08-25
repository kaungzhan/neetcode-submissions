class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = set()
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(n, parent):
            if n in visited:
                return False 
            visited.add(n)
            for nei in graph[n]:
                if nei == parent:
                    continue 
                if not dfs(nei, n):
                    return False
            return True 
        return dfs(0,-1) and len(visited) == n 

