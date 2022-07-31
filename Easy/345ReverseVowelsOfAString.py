class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = 'aAeEiIoOuU'
        vowels_in = ''
        
        for char in s:
            if char in vowels:
                vowels_in = char + vowels_in
        
        ans = ''
        i = 0
        for char in s:
            if char in vowels:
                ans = ans + vowels_in[i]
                i += 1
            else:
                ans = ans + char
                
        return ans
        
