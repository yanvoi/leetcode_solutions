# O(n) time BFS from the center, O(n) space
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        result = [[] for _ in range(rows * cols)]
        index = 0
        queue = collections.deque([[rCenter, cCenter]])
        while queue:
            row, col = queue.popleft()
            if (not 0 <= row < rows) or (not 0 <= col < cols) or visited[row][col]: continue
            visited[row][col] = True
            result[index] = [row, col]
            index += 1

            queue.append([row - 1, col])
            queue.append([row + 1, col])
            queue.append([row, col - 1])
            queue.append([row, col + 1])

        return result
