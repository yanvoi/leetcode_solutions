class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        @cache
        def solve(index):
            if index >= len(questions):
                return 0

            cur_points, to_skip = questions[index][0], questions[index][1]
            # we either skip to then next one
            # or take the current one and go to the next possible
            return max(solve(index + 1), cur_points + solve(index + to_skip + 1))

        return solve(0)
