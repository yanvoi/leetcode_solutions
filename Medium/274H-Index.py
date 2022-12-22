class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        answer = 0
        for i, num in enumerate(sorted(citations, reverse=True)):
            # same as num >= i+1
            if num > i: answer += 1

        return answer
