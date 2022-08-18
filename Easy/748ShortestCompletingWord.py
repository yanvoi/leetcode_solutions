class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        
        license_freq = dict()
        for char in licensePlate:
            if char.isalpha():
                char = char.lower()
                license_freq[char] = license_freq.get(char, 0) + 1
            
        shortest = float('inf')
        
        for word in words:
            
            word_freq = dict()
            for char in word:
                word_freq[char] = word_freq.get(char, 0) + 1
                
            is_good = True
            for char in license_freq:
                if char not in word_freq or word_freq[char] < license_freq[char]:
                    is_good = False
                    break
                    
            if is_good and len(word) < shortest:
                ans = word
                shortest = len(word)
                
        return ans
        
