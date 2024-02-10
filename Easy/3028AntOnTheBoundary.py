# O(n) time, O(1) space (depends on how accumulate is implemented)
class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        return sum(not num for num in accumulate(nums))
