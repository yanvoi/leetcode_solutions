class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ans = 0
        visited = set()
        
        for i in range(len(nums)):
            if i in visited: continue
                
            s = set()
            
            while not i in s:
                s.add(i)
                i = nums[i]
            
            visited = visited.union(s)
            ans = max(ans, len(s))
           
        return ans
    
