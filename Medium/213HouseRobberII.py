# the same solution as for the House Robber I problem
# but we loop over nums twice
# first time ignoring the last element
# and second time ignoring the first one
# since the first and last one cannot be robbed at the same night
class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1: return nums[0]

        last, cur1 = 0, 0
        for num in nums[:-1]:
            last, cur1 = cur1, max(cur1, last + num)

        last, cur2 = 0, 0
        for num in nums[1:]:
            last, cur2 = cur2, max(cur2, last + num)

        return max(cur1, cur2)
