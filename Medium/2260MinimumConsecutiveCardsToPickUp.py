class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        answer = float('inf')
        seen = dict()
        for index, value in enumerate(cards):
            if value in seen:
                answer = min(index - seen[value] + 1, answer)
                
            seen[value] = index
            
        return answer if answer != float("inf") else -1
        
