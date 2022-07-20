class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        
        def isIncreasing(arr, count):
            
            for i in range(len(arr) - 1):
                if arr[i] >=arr[i+1]:
                    count += 1
                    if count > 1:
                        return False
                    
                    return isIncreasing(arr[:i] + arr[i+1:], count) or isIncreasing(arr[:i+1] + arr[i+2:], count)
            
            return True
                
        return isIncreasing(nums, 0)
    
