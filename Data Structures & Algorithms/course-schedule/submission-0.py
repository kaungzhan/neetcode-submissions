class Solution:
    def canFinish(self, numCourses: int, prerequisites:List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course,pre in prerequisites:
            graph[course].append(pre)
        path, visited = set(), set()
        def dfs(n):
            if n in path:
                return False 
            if n in visited: 
                return True 
            path.add(n)
            neighbours = graph[n]
            for nei in neighbours:
                not_cycle = dfs(nei)
                if not not_cycle:
                    return False
            path.remove(n)
            visited.add(n)
            return True 
        for i in range(numCourses):
            finish = dfs(i)
            if not finish:
                return False
        return True 
            