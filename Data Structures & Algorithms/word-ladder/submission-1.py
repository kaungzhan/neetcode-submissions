from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        visited = set()
        graph = defaultdict(list)
        for word in wordList: 
            for i in range(len(word)):
                wc = word[:i] + '*' + word[i+1:]
                graph[wc].append(word)
        def bfs(n, d):
            q = deque()
            q.append((n, d))
            visited.add(n)
            while q:
                node, distance = q.popleft()
                if node == endWord:
                    return distance
                for j in range(len(node)):
                    wild_card = node[:j] + '*' + node[j+1:]
                    for nei in graph[wild_card]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append((nei, distance + 1))
            return 0
        return bfs(beginWord, 1) 
                
            


