class Solution:
    @cache
    def diffWaysToCompute(self, expression: str) -> List[int]:
      
        if expression.isdigit():
            return [int(expression)]

        answer = []
        for index, char in enumerate(expression):
            if char in '*-+':
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index+1:])
                answer.extend(eval(str(l) + char + str(r)) for l in left for r in right)

        return answer
        
