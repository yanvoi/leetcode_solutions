class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        totalSum = curMax = curMin = 0
        maxSum = minSum = nums[0]
        
        for num in nums:
            totalSum += num

            curMax = max(curMax + num, num)
            curMin = min(curMin + num, num)

            maxSum = max(maxSum, curMax)
            minSum = min(minSum, curMin)

        return max(maxSum, totalSum - minSum) if maxSum > 0 else maxSum
