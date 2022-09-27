class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        second = dict()
        for index, word in enumerate(list2):
            second[word] = index
            
        minimum, answer = float('inf'), []
        
        for index, word in enumerate(list1):
            if word not in second: continue
                
            curr = index + second[word]
            
            if curr < minimum:
                minimum = curr
                answer = [word]
            elif curr == minimum:
                answer.append(word)
        
        return answer
        
