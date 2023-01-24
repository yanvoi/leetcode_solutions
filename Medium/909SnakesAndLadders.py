class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        n = len(board)
        cells = [None] * (n ** 2 + 1)
        label = 1
        columns = list(range(n))
        for i in range(n - 1, -1, -1):
            for j in columns:
                cells[label] = (i, j)
                label += 1
            columns.reverse()

        dist = [-1] * (n ** 2 + 1)
        dist[1] = 0
        q = deque([1])
        while q:
            curr = q.popleft()
            for choice in range(curr + 1, min(curr + 6, n ** 2) + 1):
                i, j = cells[choice]
                next_square = board[i][j] if board[i][j] != -1 else choice

                if dist[next_square] == -1:
                    dist[next_square] = dist[curr] + 1
                    q.append(next_square)

        return dist[-1]
