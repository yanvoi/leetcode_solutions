class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        # I'm using a cool trick from a different solution I saw
        # while looping over nums: denote new 0's as -1, and new 1's as 2
        # at the end, turn all -1's to 0's, and 2's to 1's

        get_neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                live_count = 0
                for x, y in get_neighbors:
                    if 0 <= i+x < n and 0 <= j+y < m and abs(board[i+x][j+y]) == 1:
                        live_count += 1

                if board[i][j] and (live_count < 2 or live_count > 3):
                    board[i][j] = -1
                
                elif not board[i][j] and live_count == 3:
                    board[i][j] = 2

        for i in range(n):
            for j in range(m):
                if board[i][j] == -1: board[i][j] = 0
                if board[i][j] == 2: board[i][j] = 1
