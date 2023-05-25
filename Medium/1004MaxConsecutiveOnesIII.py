class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        left = 0
        zero_count = 0
        answer = 0

        for right, num in enumerate(nums):
            zero_count += not num
            if zero_count > k:
                zero_count -= not nums[left]
                left += 1
            
            answer = max(answer, right - left + 1)
        return answer
