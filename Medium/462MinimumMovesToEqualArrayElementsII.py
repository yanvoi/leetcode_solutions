class Solution:
    def minMoves2(self, nums: List[int]) -> int:

        answer = 0
        median = sorted(nums)[len(nums) // 2]
        for num in nums:
            answer += abs(num - median)

        return answer
