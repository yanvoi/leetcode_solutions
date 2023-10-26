# horrible code, I'm tired
class Solution:
    def isFascinating(self, n: int) -> bool:
        concatenation = str(n) + str(2 * n) + str(3 * n)
        return len(concatenation) == 9 and all(str(digit) in concatenation for digit in range(1, 10))
