class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur, ans = 0, 0
        
        for num in nums:
            if num == 1:
                cur += 1
            else:
                if ans < cur:
                    ans = cur
                cur = 0
        if ans < cur:
            ans = cur
        
        return ans
    
