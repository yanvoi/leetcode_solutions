class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        res = curr = sum(nums[:k])
        
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i-k]
            res = max(res, curr)
        
        return res / k
        
