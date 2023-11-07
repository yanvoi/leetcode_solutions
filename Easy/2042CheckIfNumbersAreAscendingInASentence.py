class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = [int(token) for token in s.split() if token.isdigit()]
        return all(num1 < num2 for num1, num2 in zip(nums, nums[1:]))
