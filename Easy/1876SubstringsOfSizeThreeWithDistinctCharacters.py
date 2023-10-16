# O(n) time
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        return sum(a != b and a != c and b != c for a, b, c in zip(s, s[1:], s[2:]))
