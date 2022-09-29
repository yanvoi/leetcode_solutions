class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        if color == image[sr][sc]: return image
        
        self.image = image
        self.__backtrack__(sr, sc, color, self.image[sr][sc])
        return self.image
    
    def __backtrack__(self, i, j, color, prev):
        if i < 0 or j < 0 or i >= len(self.image) or j >= len(self.image[0]) or self.image[i][j] != prev:
            return
        
        self.image[i][j] = color
        self.__backtrack__(i-1, j, color, prev)
        self.__backtrack__(i+1, j, color, prev)
        self.__backtrack__(i, j-1, color, prev)
        self.__backtrack__(i, j+1, color, prev)
        
