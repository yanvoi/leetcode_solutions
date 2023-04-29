class Solution:
    def alphabetBoardPath(self, target: str) -> str:

        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        mapping = {board[r][c] : (r, c) for r in range(len(board)) for c in range(len(board[r]))}

        answer = []
        prev_row, prev_column = (0, 0)
        
        for char in target:
            cur_row, cur_column = mapping[char]
            if cur_column < prev_column:
                answer.append("L" * (prev_column - cur_column))
            if cur_row < prev_row:
                answer.append("U" * (prev_row - cur_row))
            if cur_row > prev_row:
                answer.append("D" * (cur_row - prev_row))
            if cur_column > prev_column:
                answer.append("R" * (cur_column - prev_column))

            answer.append("!")
            prev_row, prev_column = cur_row, cur_column

        return "".join(answer)
