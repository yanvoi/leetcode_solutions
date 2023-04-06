# simple BFS from the entrance
# until we find ourselves on the edge with "." that is not the entrance
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        m, n = len(maze), len(maze[0])
        q = deque()
        q.append(entrance)
        visited = set()
        steps = 0

        while q:
            for _ in range(len(q)):
                x, y = q.popleft()

                # if we've already visited this spot
                if (x, y) in visited:
                    continue
                visited.add((x, y))

                # we're out of bounds or stuck in the wall
                if x < 0 or x >= m or y < 0 or y >= n or maze[x][y] == "+":
                    continue

                # we reach the exit which is != entrance
                if steps != 0 and (x == 0 or x == m - 1 or y == 0 or y == n - 1):
                    return steps

                # add all neighboring cells
                # (we could also check if they've been visited before)
                for xi, yi in ([-1, 0], [1, 0], [0, -1], [0, 1]):
                    q.append([x + xi, y + yi])

            steps += 1

        return -1
