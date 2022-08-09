class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h = dict()
        
        for index, num in enumerate(numbers):
            if target - num in h:
                return [h[target-num], index+1]
            h[num] = index + 1
            
        return []
        
