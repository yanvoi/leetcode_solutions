class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def search_left(arr, val):
            left, right = 0, len(arr) - 1
            
            while left <= right:
                mid = (left + right) // 2
                if val > arr[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return left
        
        def search_right(arr, val):
            left, right = 0, len(arr) - 1
            
            while left <= right:
                mid = (left + right) // 2
                
                if val >= arr[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return right
                    
        left, right = search_left(nums, target), search_right(nums, target)
        return [left, right] if left <= right else [-1, -1]
        
