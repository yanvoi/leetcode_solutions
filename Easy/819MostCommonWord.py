class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        banned = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        freq = dict()
        
        for word in words:
            if word in banned: continue
                
            freq[word] = freq.get(word, 0) + 1
                
        return max(freq, key=freq.get) 
        
