class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        x, y = sorted(list(s1)), sorted(list(s2))
        return all(n1 >= n2 for n1, n2 in zip(x, y)) or all(n2 >= n1 for n1, n2 in zip(x, y))
