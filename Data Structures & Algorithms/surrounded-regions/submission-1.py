class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, columns = len(board), len(board[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        def dfs(r,c):
            if (r < 0 or 
                c < 0 or 
                r >= rows or 
                c >= columns or
                board[r][c] == "#" or 
                board[r][c] == "X"):
                    return 
            board[r][c] = "#"
            for dr,dc in directions:
                dfs(r + dr, c + dc)
        for r in range(rows):
            for c in range(columns):
                if ((r == 0 or
                    c == 0 or 
                    r == rows - 1 or 
                    c == columns - 1) and
                    board[r][c] == "O"
                ):
                    dfs(r,c)
        for a in range(rows):
            for b in range(columns):
                if board[a][b] == "#":
                    board[a][b] = "O"
                elif board[a][b] == "O":
                    board[a][b] = "X"
            
