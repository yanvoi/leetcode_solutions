class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        answer = []
        
        i = len(s) - 1
        while i > -1:
            if s[i] == '#':
                i = i - 2
                code = int(s[i:i+2])
            else:
                code = int(s[i])
            
            answer.append(chr(code + 96))
            i = i - 1
            
        return ''.join(answer[::-1]) 
      
