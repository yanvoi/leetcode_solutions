class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        biggest = 0
        for candy in candies:
            if candy > biggest:
                biggest = candy
                
        answer = []
        for candy in candies:
            if candy + extraCandies >= biggest:
                answer.append(True)
            else:
                answer.append(False)
                
        return answer
        
