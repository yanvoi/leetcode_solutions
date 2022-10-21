class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        seen_at = dict()
        
        for i in range(len(nums)):
            if nums[i] in seen_at and i - seen_at[nums[i]] <= k:
                return True
            seen_at[nums[i]] = i
        
        return False
        
