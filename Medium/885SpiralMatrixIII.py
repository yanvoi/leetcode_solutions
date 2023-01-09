class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        coordinates = set(((row, col) for row in range(rows) for col in range(cols)))
        to_add = rows * cols
        answer = [[rStart, cStart]]
        i, j = rStart, cStart
        move = 1

        while to_add > 0:
            # go right
            for _ in range(move):
                j += 1
                if (i, j) in coordinates:
                    answer.append([i, j])

            # go down
            for _ in range(move):
                i += 1
                if (i, j) in coordinates:
                    answer.append([i, j])

            # go left
            for _ in range(move + 1):
                j -= 1
                if (i, j) in coordinates:
                    answer.append([i, j])

            # go up
            for _ in range(move + 1):
                i -= 1
                if (i, j) in coordinates:
                    answer.append([i, j])

            # next circle is gonna be bigger
            move += 2
            to_add = (rows * cols) - len(answer)

        return answer
        
