class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        self.copy = mat
        for _ in range(4):
            self.__rotate__()
            if self.copy == target: return True
            
        return False
    
    
    def __rotate__(self):
        
        for i in range(len(self.copy)):
            for j in range(i+1, len(self.copy)):
                self.copy[i][j], self.copy[j][i] = self.copy[j][i], self.copy[i][j]
                
        for i in range(len(self.copy)):
            for j in range(len(self.copy) // 2):
                self.copy[i][j], self.copy[i][-j-1] = self.copy[i][-j-1], self.copy[i][j]
        
