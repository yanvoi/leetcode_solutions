class Solution:
    def totalMoney(self, n: int) -> int:
        return sum(day % 7 + day // 7 + 1 for day in range(n))
