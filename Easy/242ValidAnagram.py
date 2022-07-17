class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        first = dict()
        second = dict()
        
        for letter in s:
            if letter in first:
                first[letter] += 1
            else:
                first[letter] = 1
                
        for letter in t:
            if letter in second:
                second[letter] += 1
            else:
                second[letter] = 1
            
        for i in first:
            if not i in second or not first[i] == second[i]:
                return False
            
        return True
        
