class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        values = [float('-inf'), float('-inf'), float('-inf')]
        
        for num in nums:
            if num not in values:
                if num > values[0]:
                    values = [num, values[0], values[1]]
                elif num > values[1]:
                    values = [values[0], num, values[1]]
                elif num > values[2]:
                    values = [values[0], values[1], num]
                    
        if float('-inf') in values:
            return values[0]
        
        return values[2]
        
