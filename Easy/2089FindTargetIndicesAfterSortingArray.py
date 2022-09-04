class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        smaller, equal = 0, 0
        
        for num in nums:
            if num == target:
                equal += 1
            elif num < target:
                smaller += 1
                
        return list(range(smaller, smaller + equal))
        
