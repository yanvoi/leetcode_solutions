class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        elements = dict()
        
        for el in nums:
            if el in elements:
                elements[el] += 1
            else:
                elements[el] = 1
                
        for el in elements:
            if elements[el] == len(nums) // 2:
                return el
        
