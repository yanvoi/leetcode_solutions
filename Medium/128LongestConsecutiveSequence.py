class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ans = 0
        s = set(nums)
        
        for num in s:
            if num - 1 in s: continue
                
            cur_num = num
            cur_streak = 1
            
            while cur_num + 1 in s:
                cur_streak += 1
                cur_num += 1
                
            ans = max(ans, cur_streak)
            
        return ans
        
