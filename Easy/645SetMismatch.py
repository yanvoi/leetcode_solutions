class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        freq, count, double = dict(), n * (n+1) // 2, 0
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] == 2:
                double = num
            else:
                count -= num
                
        return [double, count]
        
