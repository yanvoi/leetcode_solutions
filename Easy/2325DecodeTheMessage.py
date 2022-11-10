class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        first_appearance = dict()
        i = 0
        for char in key:
            if char in first_appearance or char == ' ':
                continue
                
            first_appearance[char] = i
            i += 1
            
        ans = []
        for char in message:
            if char == ' ':
                ans.append(' ')
            else:
                ans.append(chr(first_appearance[char] + 97))
                
        return ''.join(ans)
        
