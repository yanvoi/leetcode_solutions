class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:

        left_sum, right_sum, n, answer = 0, sum(nums), len(nums), []

        for i, num in enumerate(nums):
            answer.append(num * i - left_sum + right_sum - num * (n - i))
            left_sum += num
            right_sum -= num

        return answer
