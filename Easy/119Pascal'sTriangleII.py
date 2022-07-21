class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        answer = []
        
        for row in range(rowIndex + 1):
            answer.append([])
            for col in range(row + 1):
                if col == 0 or col == row:
                    answer[row].append(1)
                else:
                    answer[row].append(answer[row-1][col-1] + answer[row-1][col])
                    
        return answer[rowIndex]
    
