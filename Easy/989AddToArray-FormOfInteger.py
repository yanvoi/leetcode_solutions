class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        string = ""
        for number in num:
            string = string + str(number)
            
        number = int(string)
        number += k
        number = str(number)
        
        answer = []
        
        for char in number:
            answer.append(char)
            
        return answer
        
