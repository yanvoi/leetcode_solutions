class Solution:
    def countDigits(self, num: int) -> int:
        return sum(not num % int(digit) for digit in str(num))
