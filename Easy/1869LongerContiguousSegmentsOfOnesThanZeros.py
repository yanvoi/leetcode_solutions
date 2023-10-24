# O(n) time, O(1) space
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        if len(s) == 1: return s[0] == "1"
        zeros_answer, ones_answer, zeros_cur, ones_cur = 0, 0, 0, 0
        prev = "!"
        for bit in s:
            if bit == prev:
                if bit == "0":
                    zeros_cur += 1
                    zeros_answer = max(zeros_answer, zeros_cur)
                else:
                    ones_cur += 1
                    ones_answer = max(ones_answer, ones_cur)
            else:
                if bit == "0":
                    zeros_cur = 0
                else:
                    ones_cur = 0
            prev = bit

        return ones_answer > zeros_answer
