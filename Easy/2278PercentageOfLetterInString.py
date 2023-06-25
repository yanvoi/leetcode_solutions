class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return math.floor((s.count(letter) / len(s)) * 100)
