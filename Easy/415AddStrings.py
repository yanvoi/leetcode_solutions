class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        answer = ""
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        for i in range(max(len(num1), len(num2))):
            
            first = num1[i] if i < len(num1) else 0
            second = num2[i] if i < len(num2) else 0
            val = int(first) + int(second) + carry
            
            answer = answer + (str(val % 10))
            carry = val // 10
            
        if carry != 0:
            answer = answer + str(carry)
        
        return answer[::-1]
        
