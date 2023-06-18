class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:

        nums.sort()
        return min(num2 - num1 for num1, num2 in zip(nums, nums[1:]))
