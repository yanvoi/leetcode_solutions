class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        ans = nums[0]
        maxi = ans
        mini = ans
        
        for i in range(1, len(nums)):
            
            candidates = (nums[i], nums[i] * maxi, nums[i] * mini)
            
            maxi = max(candidates)
            mini = min(candidates)
            
            ans = max(ans, maxi)
            
        return ans
        
