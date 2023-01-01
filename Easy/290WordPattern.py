class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split()
        if len(words) != len(pattern):
            return False
        
        match, reverse = dict(), dict()
        for char, word in zip(pattern, words):
            if (char in match and match[char] != word) or (word in reverse and reverse[word] != char):
                return False
            match[char] = word
            reverse[word] = char
                
        return True
        
