class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.nums = nums
        return self._sums(0, 0)

    def _sums(self, index, xor_sum):
        if index == len(self.nums):
            return xor_sum

        return self._sums(index + 1, xor_sum) + \
               self._sums(index + 1, xor_sum ^ self.nums[index]) 
        
