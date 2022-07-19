class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = (''.join(char for char in s if char.isalnum())).lower()
        
        if s == s[::-1]:
            return True
        
        return False
        
