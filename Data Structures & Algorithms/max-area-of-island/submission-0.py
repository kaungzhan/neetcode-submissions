class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        directions = [[0,1], [-1,0], [1,0], [0,-1]]
        area = 0
        def bfs(r,c):
            count = 1
            q = deque()
            q.append((r,c))
            grid[r][c] = 0
            while q: 
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nc < 0 or nr >= rows or
                        nc >= columns or grid[nr][nc] == 0
                    ):
                        continue
                    count += 1
                    q.append((nr, nc))
                    grid[nr][nc] = 0
            return count

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    area = max(area, bfs(r, c))
        return area
