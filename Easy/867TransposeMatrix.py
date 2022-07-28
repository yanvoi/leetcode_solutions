class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        answer = [[]]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if not j < len(answer):
                    answer.append([])
                answer[j].append(matrix[i][j])
                    
        return answer        
        
