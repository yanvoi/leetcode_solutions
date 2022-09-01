class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        ans = [-1] * len(nums)
        stack = []
        
        for i in range((len(nums) * 2) - 1, -1, -1):
            
            while stack and stack[-1] <= nums[i % len(nums)]:
                stack.pop()
                
            if stack:
                ans[i % len(nums)] = stack[-1]
                
            stack.append(nums[i % len(nums)])
            
        return ans
        
