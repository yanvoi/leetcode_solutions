class Solution:
    def countElements(self, nums: List[int]) -> int:
        min_num, max_num = min(nums), max(nums)
        return sum(num != min_num and num != max_num for num in nums)
