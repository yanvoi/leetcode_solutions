class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        first = second = target = ''
        
        for char in firstWord:
            first += str(ord(char) - 97)
        
        for char in secondWord:
            second += str(ord(char) - 97)
            
        for char in targetWord:
            target += str(ord(char) - 97)
        
        return (int(first) + int(second)) == int(target)
        
