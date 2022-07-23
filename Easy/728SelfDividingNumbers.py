class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        answer = []
        
        for number in range(left, right + 1):
            copy = number
            add = True
            while copy > 0:
                digit = copy % 10
                if digit == 0 or number % digit != 0:
                    add = False
                    break
                copy = copy // 10
            if add:
                answer.append(number)
                
        return answer
        
