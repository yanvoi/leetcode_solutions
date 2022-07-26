class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for row in image:
            row = row.reverse()
            
        for i in range(len(image)):
            for j in range(len(image)):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
                    
        return image
