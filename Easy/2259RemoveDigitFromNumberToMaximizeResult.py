# O(n) time
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        for i in range(len(number) - 1):
            if number[i] == digit and number[i] < number[i + 1]:
                return number[:i] + number[i + 1:]
            
        index = number.rfind(digit)
        return number[:index] + number[index + 1:]
        
