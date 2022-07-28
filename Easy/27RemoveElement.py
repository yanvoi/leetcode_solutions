class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums.insert(0, nums[i])
                nums.pop(i+1)
                count += 1
                
        return count
    
