class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        return max(nums_sorted[i] + nums_sorted[~i] for i in range(len(nums) // 2))
