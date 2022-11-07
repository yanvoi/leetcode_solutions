class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        # we're using the fact that nums are in the range [1, n]
        ans = []
        for num in nums:
            if nums[abs(num)-1] < 0:
                ans.append(abs(num))
            else:
                nums[abs(num)-1] = nums[abs(num)-1] * (-1)
                
        return ans
        
