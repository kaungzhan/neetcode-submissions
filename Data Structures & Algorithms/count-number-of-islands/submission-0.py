class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, coln = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        island = 0
        visited = set()
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= coln or (r,c)               in visited or grid[r][c] == "0"):             
                return 
            visited.add((r, c))
            for dr,dc in directions:
                dfs(r + dr, c + dc)


        for r in range(rows):
            for c in range(coln):
                if (grid[r][c] == "1" and
                    (r,c) not in visited):
                    dfs(r, c)
                    island += 1        
        return island