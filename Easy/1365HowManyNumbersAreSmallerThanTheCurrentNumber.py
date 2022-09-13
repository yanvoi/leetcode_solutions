class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        indeces = dict()
        for i, num in enumerate(sorted(nums)):
            if num in indeces: continue
            indeces[num] = i
            
        return [indeces[num] for num in nums]
        
