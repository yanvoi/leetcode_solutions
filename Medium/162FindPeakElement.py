class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        top = len(nums) - 1
        
        while low <= top:
            
            mid = (low + top) // 2
            
            if (mid == 0 or nums[mid] > nums[mid-1]) and (mid == len(nums) - 1 or nums[mid] > nums[mid+1]):
                return mid
            
            elif mid == len(nums) - 1 or nums[mid] > nums[mid+1]:
                top = mid - 1
            
            else:
                low = mid + 1
                
        return -1
        
