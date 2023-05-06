class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        modulus = 10 ** 9 + 7
        nums.sort()
        left, right = 0, len(nums) - 1
        answer = 0

        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                answer = (answer + pow(2, right - left)) % modulus
                left += 1

        return answer
