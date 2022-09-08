class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return nums.index(target) if target in nums else -1
        
        # find the smallest element and adjust the left and right pointers accordingly
        # first if statement checks whether the array is sorted, if it is, we do simple binary search
        n = len(nums)
        if nums[0] < nums[-1]:
            left, right = 0, n - 1
        else:
            left, right = 0, n - 1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] >= nums[-1]:
                    left = mid + 1
                elif nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
                    break
                else:
                    right = mid - 1
            
            if target > nums[-1]:
                left, right = 0, mid - 1
            else:
                left, right = mid, n - 1
                
        # now that we know in which sorted part of the array
        # we need to look for the target element
        # we do simple binary search
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        if left < n and nums[left] == target: return left
        
        return -1
        
