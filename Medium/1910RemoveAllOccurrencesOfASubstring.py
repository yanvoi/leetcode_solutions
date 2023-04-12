# lazy solution
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        while part in s:
            s = s.replace(part, '', 1)

        return s

# to do: learn the Knuth–Morris–Pratt algorithm
# for pattern searching
# https://www.youtube.com/watch?v=V5-7GzOfADQ
