class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        needed = len(nums) * (len(nums) + 1) // 2
        seen, repeated = set(), -1
        
        for num in nums:
            if num in seen:
                repeated = num
            else:
                seen.add(num)
                needed -= num
                
        return [repeated, needed]
        
