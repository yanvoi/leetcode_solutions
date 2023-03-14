class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        min_index, max_index = nums.index(min(nums)), nums.index(max(nums))

        delete_from_left = max(min_index, max_index) + 1
        delete_from_right = len(nums) - min(min_index, max_index)
        delete_from_both_sides = min(min_index, max_index) + 1 + len(nums) - max(min_index, max_index)

        return min(delete_from_left, delete_from_right, delete_from_both_sides)
