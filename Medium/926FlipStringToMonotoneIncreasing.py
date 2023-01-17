class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:

        answer, ones_count = 0, 0
        for char in s:
            if char == '1':
                ones_count += 1
            else:
                # we either flip all the previous 1's to 0's
                # or we keep on flipping next 0's to 1's
                answer = min(ones_count, answer + 1)

        return answer
