class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:

        left_sum, right_sum, answer = 0, sum(nums), []

        for i, num in enumerate(nums):
            # thanks to the list being sorted
            answer.append(num * i - left_sum + right_sum - num * (len(nums) - i))
            left_sum += num
            right_sum -= num

        return answer
