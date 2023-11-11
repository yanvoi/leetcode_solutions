class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        cur_answer, answer, last = 0, 0, float("-inf")
        for num in nums:
            if num > last: cur_answer += num
            else: cur_answer = num
            last = num
            answer = max(answer, cur_answer)

        return answer
