# O(1) time, O(1) space
# sum(all integers <= n) - 2 * sum(all integers divisible by m and <= n)
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return ((n * (n + 1)) // 2) - 2 * (((2 * m) + (((n // m) - 1) * m)) * (n // m) // 2)
