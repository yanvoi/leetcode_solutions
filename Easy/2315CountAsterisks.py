class Solution:
    def countAsterisks(self, s: str) -> int:

        count = 0
        even = True
        for char in s:
            if char == "|": even = not even
            elif char == "*" and even: count += 1

        return count
