class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums: row.sort()
        return sum(max(nums[row][col] for row in range(len(nums))) for col in range(len(nums[0])))
