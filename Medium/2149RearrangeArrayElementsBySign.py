class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        return [num for pair in zip((i for i in nums if i >= 0), (j for j in nums if j < 0)) for num in pair]
