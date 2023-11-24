class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums_set = set()
        for num in nums: nums_set ^= {num}
        return not nums_set
