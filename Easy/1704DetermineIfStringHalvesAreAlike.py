class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("aeiouAEIOU")
        return sum(char in vowels for char in s[:len(s)//2]) == sum(char in vowels for char in s[len(s)//2:])
