class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        return sorted(range(lo, hi + 1), key=lambda x: (self.power(x), x))[k - 1]


    @cache
    def power(self, num):
        if num == 1:
            return 0

        return 1 + self.power(num // 2) if num % 2 == 0 else 1 + self.power((num * 3) + 1)
