class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        chars_freq = dict()
        for char in chars:
            chars_freq[char] = chars_freq.get(char, 0) + 1
            
        ans = 0
        for word in words:
            word_freq = dict()
            add = True
            
            for char in word:
                if char not in chars_freq:
                    add = False
                    break
                    
                word_freq[char] = word_freq.get(char, 0) + 1
                
            for char in word_freq:
                if word_freq[char] > chars_freq[char]:
                    add = False
                    break
                    
            if add: ans += len(word)
            
        return ans
        
