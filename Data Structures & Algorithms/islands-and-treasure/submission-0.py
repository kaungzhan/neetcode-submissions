from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, columns = len(grid), len(grid[0])
        queue = deque()
        visited = set()
        distance = [[-1] * columns for _ in range(rows)]
    
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))
                    distance[r][c] = 0
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            r, c = queue.popleft()
            for dr,dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 
                0 <= nc < columns and 
                (nr, nc) not in visited and 
                grid[nr][nc] != -1):
                    visited.add((nr,nc))
                    distance[nr][nc] = distance[r][c] + 1
                    queue.append((nr,nc))
                    grid[nr][nc] =  distance[nr][nc]
        
