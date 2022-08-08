class Solution:
    def findMin(self, nums: List[int]) -> int:
        # edge cases
        if len(nums) == 1: return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        
        left, right = 1, len(nums) - 1
        first = nums[0]
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid] > nums[mid-1] and nums[mid] > first:
                left = mid + 1
            else:
                right = mid - 1
        
        return nums[mid]
        
