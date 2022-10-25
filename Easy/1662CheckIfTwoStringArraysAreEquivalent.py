class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        for c1, c2 in zip(self.__generate__(word1), self.__generate__(word2)):
            if c1 != c2:
                return False
            
        return True
    
    
    # generators allow us to solve the problem with O(1) space complexity
    def __generate__(self, arr):
        
        for word in arr:
            for char in word:
                yield char
                
        yield None
    
    
 class SecondSolution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        return ''.join(word1) == ''.join(word2)
    
