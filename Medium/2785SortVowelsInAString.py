class Solution:
    def sortVowels(self, s: str) -> str:
        vowels_set = set("aeiouAEIOU")
        vowels = sorted([char for char in s if char in vowels_set], reverse=True)
        return "".join(vowels.pop() if char in vowels_set else char for char in s)
