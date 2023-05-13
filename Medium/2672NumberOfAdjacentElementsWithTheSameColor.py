class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:

        colored = [0] * n
        answer = [0] * len(queries)
        cur_answer = 0

        for i, (index, color) in enumerate(queries):
            if index > 0 and colored[index - 1]:
                cur_answer -= colored[index - 1] == colored[index]
                cur_answer += colored[index - 1] == color
            if index < n - 1 and colored[index + 1]:
                cur_answer -= colored[index + 1] == colored[index]
                cur_answer += colored[index + 1] == color

            colored[index] = color
            answer[i] = cur_answer

        return answer
