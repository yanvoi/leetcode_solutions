class Solution:
    def averageValue(self, nums: List[int]) -> int:
        
        count = to_sum = 0
        
        for num in nums:
            if num % 2 == 0 and num % 3 == 0:
                count += 1
                to_sum += num
                
        return to_sum // count if count > 0 else 0
        
