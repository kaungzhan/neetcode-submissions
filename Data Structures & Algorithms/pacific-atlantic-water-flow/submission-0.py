class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, columns = len(heights), len(heights[0])
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        pac, atl = set(), set()
        def dfs(r,c , visited, prevHeight):
            if(r < 0 or 
               c < 0 or 
               r >= rows or
               c >= columns or 
               (r,c) in visited or
               heights[r][c] < prevHeight):
                return 
            visited.add((r,c))
            for dr,dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])
        for r in range(rows):
            for c in range(columns):
                if r == 0 or c == 0:
                    dfs(r, c, pac, heights[r][c])
                if r == rows-1 or c == columns-1:
                    dfs(r, c, atl, heights[r][c])
        return [(i, j) for i in range(rows) for j in range(columns) 
        if (i, j) in pac and (i, j) in atl]
        
        