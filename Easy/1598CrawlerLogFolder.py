# O(n) time, O(1) space
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        answer = 0
        for log in logs:
            if log[:2] == "..":
                answer -= 1 if answer else 0
            elif log[0] != '.':
                answer += 1

        return answer
