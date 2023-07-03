class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        def digit_sum(num):
            cur_sum = 0
            while num:
                cur_sum += num % 10
                num //= 10
            return cur_sum

        return abs(sum(nums) - sum(digit_sum(num) for num in nums))
