class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        numbers_in_the_array = set(nums)
        
        return [i for i in range(1, len(nums) + 1) if not i in numbers_in_the_array]
        
