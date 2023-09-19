class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = set("aeiou")
        return sum(word[0] in vowels and word[-1] in vowels and left <= i <= right for i, word in enumerate(words))
