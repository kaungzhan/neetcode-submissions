class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for cour,pre in prerequisites:
            graph[cour].append(pre)
        path, visited = set(), set()
        valid = []
        def dfs(n):
            if n in path:
                return False
            if n in visited:
                return True 
            path.add(n)
            neighbors = graph[n]
            for nei in neighbors:
                if not dfs(nei):
                    return False
            path.remove(n)
            valid.append(n)
            visited.add(n)
            return True 
        for i in range(numCourses):
            if not dfs(i):
                return []
        return valid
        


        