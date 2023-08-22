class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        @cache
        def sum_digits(num):
            return num % 10 + sum_digits(num // 10) if num else 0

        return max(Counter(sum_digits(num) for num in range(lowLimit, highLimit + 1)).values())
