class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if len(digits) == 0:
            return []
        
        add = 1
        iterate = len(digits) - 1
        
        while add != 0 and iterate > 0:
            digits[iterate] += 1
            
            if not digits[iterate] % 10 == 0:
                add = 0
                
            digits[iterate] = digits[iterate] % 10
            iterate -= 1
            
        if add == 1:
            digits[0] += 1
            if digits[0] % 10 == 0:
                digits[0] = 0
                digits.insert(0, 1)
            
        return digits
        
