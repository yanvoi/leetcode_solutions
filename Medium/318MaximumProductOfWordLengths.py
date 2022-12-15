class Solution:
    def maxProduct(self, words: List[str]) -> int:

        # for every word, assing it the set of it's characters
        char_set = dict()
        for i, word in enumerate(words):
            char_set[word] = set(word)
            
        
        ans = 0
        for i, first in enumerate(words):
            for j, second in enumerate(words[i+1:]):
                if char_set[first].isdisjoint(char_set[second]):
                    ans = max(ans, len(first) * len(second))
                
        return ans
        
