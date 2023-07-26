class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        answer = 0
        count = defaultdict(int)
        for num in nums:
            answer += count[num - k]
            answer += count[num + k]
            count[num] += 1

        return answer
