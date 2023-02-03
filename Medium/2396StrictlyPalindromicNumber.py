class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:

        self.n = n
        for i in range(2, n - 1):
            converted = self.numberToBase(i)
            if converted != converted[::-1]:
                return False

        return True


    def numberToBase(self, base):

        digits = []
        n = self.n
        while n:
            digits.append(int(n % base))
            n //= base

        return digits
