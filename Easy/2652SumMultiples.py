class Solution:
    def sumOfMultiples(self, n: int) -> int:
        return sum(num if num % 3 == 0 or num % 5 == 0 or num % 7 == 0 else 0 for num in range(1, n+1))
