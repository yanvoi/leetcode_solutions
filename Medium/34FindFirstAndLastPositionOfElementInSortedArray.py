class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def search(leftMost):
            left, right, answer = 0, len(nums) - 1, -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    answer = mid
                    if leftMost:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return answer
        
        return [search(True), search(False)]
        
