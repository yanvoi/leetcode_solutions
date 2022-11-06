class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        unique = set(nums)
        
        for num in (int(str(num)[::-1]) for num in nums):
            unique.add(num)
            
        return len(unique)
        
