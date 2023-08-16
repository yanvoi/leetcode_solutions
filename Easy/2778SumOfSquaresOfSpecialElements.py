class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        return sum(num ** 2 for num, i in zip(nums, range(1, len(nums) + 1)) if len(nums) % i == 0)
