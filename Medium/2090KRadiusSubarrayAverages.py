# O(n) time, O(n) space - using left_sum of the input list
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        left_sum = [num for num in nums]
        for i in range(1, n):
            left_sum[i] += left_sum[i - 1]

        avgs = [-1] * n
        for i in range(k, n - k):
            avgs[i] = (left_sum[i + k] - left_sum[i - k] + nums[i - k]) // (2 * k + 1)

        return avgs
