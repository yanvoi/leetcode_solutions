# O(n) time, O(1) space
class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        answer = float("-inf")
        for i in range(len(nums) -1, -1, -1):
            num = nums[i]
            if num <= answer:
                answer += num
            else:
                answer = num

        return answer
