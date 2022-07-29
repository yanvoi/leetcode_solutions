class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        mapping = dict()
        for i in range(len(s)):
            if s[i] in mapping:
                mapping[s[i]].append(i)
            else:
                mapping[s[i]] = [i]
                
        second = dict()
        for i in range(len(t)):
            if t[i] in second:
                second[t[i]].append(i)
            else:
                second[t[i]] = [i]
                
        for el in mapping.values():
            if not el in second.values():
                return False
        
        return True
        
