class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        helping = [el for row in mat for el in row]
        if r * c != len(helping):
            return mat
        
        answer = []
        
        for i in range(0, len(helping), c):
            answer.append(helping[i:i+c])
            
        return answer
        
