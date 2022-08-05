class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        mid = 0
        
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                mid = i+1
                break
        
        nums = nums[mid:] + nums[:mid]
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
        
