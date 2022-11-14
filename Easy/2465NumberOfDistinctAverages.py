class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        
        nums.sort()
        left, right = 0, len(nums) - 1
        distinct = set()
        
        while left < right:
            distinct.add((nums[left] + nums[right]) / 2)
            left += 1
            right -= 1
        
        return len(distinct)
        
