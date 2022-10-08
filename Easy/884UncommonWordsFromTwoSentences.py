class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        first = s1.split()
        second = s2.split()
        
        dict1 = dict()
        dict2 = dict()
        
        for char in first:
            dict1[char] = dict1.get(char, 0) + 1
            
        for char in second:
            dict2[char] = dict2.get(char, 0) + 1
        
        uncommon = []
        
        for word in dict1:
            if word not in dict2 and dict1[word] == 1:
                uncommon.append(word)
                
        for word in dict2:
            if word not in dict1 and dict2[word] == 1:
                uncommon.append(word)
                
        return uncommon
    
