# O(n) time, O(1) space
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        answer = 0
        for i in range(1, len(nums)):
            answer += nums[i - 1] - nums[i] + 1 if nums[i - 1] >= nums[i] else 0
            nums[i] = nums[i - 1] + 1 if nums[i - 1] >= nums[i] else nums[i]

        return answer
