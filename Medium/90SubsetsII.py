class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        if not nums: return []
        
        nums.sort()
        ans, cur = [[]], []
        
        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i-1]:
                cur = [item + [nums[i]] for item in cur]
            else:
                cur = [item + [nums[i]] for item in ans]
            
            ans += cur
            
        return ans
        
