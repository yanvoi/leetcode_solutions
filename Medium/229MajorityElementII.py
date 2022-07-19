class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        dictionary = dict()
        
        for i in range(len(nums)):
            if nums[i] in dictionary:
                dictionary[nums[i]] += 1
            else:
                dictionary[nums[i]] = 1
                
        major_elements = []
                
        for el in dictionary:
            if dictionary[el] > len(nums) / 3:
                major_elements.append(el)
        
        return major_elements
    
