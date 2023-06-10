class Solution:
    def partitionString(self, s: str) -> int:

        answer = 1
        cur_chars = set()
        for char in s:
            if char in cur_chars:
                answer += 1
                cur_chars = set()
            cur_chars.add(char)

        return answer
