class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        # I create a dictionary for every word in words, where I store frequency of each character in that word
        
        cur_freq = dict()
        for char in words[0]:
            cur_freq[char] = cur_freq.get(char, 0) + 1
            
        for word in words[1:]:
            
            sec_freq = dict()
            for char in word:
                sec_freq[char] = sec_freq.get(char, 0) + 1
                
            for char in cur_freq:
                if cur_freq[char] != 0 and char in sec_freq:
                    cur_freq[char] = min(cur_freq[char], sec_freq[char])
                else:
                    cur_freq[char] = 0
              
        ans = []
        for char in cur_freq:
            for _ in range(cur_freq[char]):
                ans.append(char)
                
        return ans
        
