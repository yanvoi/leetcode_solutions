class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        ans = []
        zeroes = 0
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
                
            if nums[i] == 0:
                zeroes += 1
            else:
                ans.append(nums[i])
                
        ans.append(nums[-1])
        return ans + [0] * zeroes
        
