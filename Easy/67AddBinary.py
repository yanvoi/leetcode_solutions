class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        answer = ""
        carry = 0
        
        a = a[::-1]
        b = b[::-1]
        
        for i in range(max(len(a), len(b))):
            
            digitA = int(a[i]) if i < len(a) else 0
            digitB = int(b[i]) if i < len(b) else 0
            
            answer = str((digitA + digitB + carry) % 2) + answer
            carry = (digitA + digitB + carry) // 2
            
        if carry != 0:
            answer = str(carry) + answer
            
        return answer
        
