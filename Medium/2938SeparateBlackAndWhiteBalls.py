# O(n) time, O(1) space
class Solution:
    def minimumSteps(self, s: str) -> int:
        black_count, answer = 0, 0
        for color in s:
            if color == '1': black_count += 1
            else: answer += black_count

        return answer
