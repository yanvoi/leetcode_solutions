class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        available_nums = dict()
        for char in magazine:
            if char in available_nums:
                available_nums[char] += 1
            else:
                available_nums[char] = 1
                
        needed_nums = dict()
        for char in ransomNote:
            if not char in available_nums:
                return False
            
            if char in needed_nums:
                needed_nums[char] += 1
            else:
                needed_nums[char] = 1
                
        for letter in needed_nums:
            if needed_nums[letter] > available_nums[letter]:
                return False
            
        return True
        
