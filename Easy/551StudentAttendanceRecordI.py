class Solution:
    def checkRecord(self, s: str) -> bool:
        
        num_of_As, consecutive_Ls = 0, 0
        
        for char in s:
            if char == 'L': consecutive_Ls += 1
            elif char == 'A': num_of_As += 1
                
            if num_of_As >= 2 or consecutive_Ls >= 3: return False
            
            if char != 'L': consecutive_Ls = 0
            
        return True
        
