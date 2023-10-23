# O(n) time, O(n) space
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        left_min, right_min = [0] * n, [0] * n
        prev_left_min, prev_right_min = float("inf"), float("inf")
        for i in range(n):
            left_min[i], prev_left_min = prev_left_min, min(prev_left_min, nums[i])
            right_min[n - i - 1], prev_right_min = prev_right_min, min(prev_right_min, nums[n - i - 1])

        candidates = [i + j + k for i, j, k in zip(left_min, nums, right_min) if i < j > k]
        result = min(candidates + [float("inf")])
        return result if result != float("inf") else -1
