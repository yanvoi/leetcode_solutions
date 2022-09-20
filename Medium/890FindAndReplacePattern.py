class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        patt_len = len(set(pattern))
        answer = []
        
        for word in words:
            if len(set(word)) != patt_len: continue
            
            to_add = True
            mapped = dict()
            
            for i in range(len(word)):
                if word[i] not in mapped:
                    if pattern[i] in mapped.values():
                        to_add = False
                        break
                    mapped[word[i]] = pattern[i]
                elif mapped[word[i]] != pattern[i]:
                    to_add = False
                    break
            
            if to_add: answer.append(word)
                
        return answer
        
