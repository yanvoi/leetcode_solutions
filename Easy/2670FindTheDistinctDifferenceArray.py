class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        distinct_left_count, distinct_right_count = [0] * n, [0] * (n + 1)
        left_distinct, right_distinct = set(), set()

        for i in range(n):
            left_distinct.add(nums[i])
            distinct_left_count[i] = len(left_distinct)

            j = n - i - 1
            right_distinct.add(nums[j])
            distinct_right_count[j] = len(right_distinct)

        return [left - right for left, right in zip(distinct_left_count, distinct_right_count[1:])]
