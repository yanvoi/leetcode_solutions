class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        copy = heights.copy()
        heights.sort()
        answer = 0
        
        for i in range(len(heights)):
            if heights[i] != copy[i]:
                answer += 1
        
        return answer
        
