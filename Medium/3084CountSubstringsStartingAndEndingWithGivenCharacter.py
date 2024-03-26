# O(n) time, O(1) space
class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        count = s.count(c)
        return ((count + 1) * count) // 2
