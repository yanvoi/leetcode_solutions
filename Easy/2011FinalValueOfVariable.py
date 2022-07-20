class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        answer = 0
        
        for operation in operations:
            
            if operation == 'X++' or operation == '++X':
                answer += 1
            else:
                answer -= 1
                
        return answer
    
