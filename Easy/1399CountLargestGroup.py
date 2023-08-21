class Solution:
    def countLargestGroup(self, n: int) -> int:
        @cache
        def sum_digits(num):
            return num % 10 + sum_digits(num // 10) if num else 0

        count = Counter([sum_digits(num) for num in range(1, n + 1)])
        largest = max(count.values())
        return sum(num == largest for num in count.values())
