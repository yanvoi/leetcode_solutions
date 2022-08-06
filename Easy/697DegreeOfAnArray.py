class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        h, left, right = dict(), dict(), dict()
        
        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i
            
            if num in h:
                h[num] += 1
            else:
                h[num] = 1
            
                
        degree = max(h.values())
        ans = len(nums)
        
        for el in h:
            if h[el] == degree:
                ans = min(ans, right[el] - left[el] + 1)
                
        return ans
        
