class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        answer = []
        
        while columnNumber > 0:
            answer.append(letters[(columnNumber % 26) - 1])
            columnNumber = (columnNumber - 1) // 26
            
        return ''.join(answer[::-1])
        
