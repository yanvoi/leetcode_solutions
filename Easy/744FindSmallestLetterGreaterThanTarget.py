class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        
        left, right = 0, len(letters) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if target >= letters[mid]:
                left = mid + 1
            else:
                right = mid - 1
                
        if letters[right] <= target:
            return letters[right+1]
                
        return letters[right]
        
