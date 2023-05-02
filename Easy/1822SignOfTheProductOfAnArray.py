class Solution:
    def arraySign(self, nums: List[int]) -> int:

        negative_count = 0
        for num in nums:
            if num == 0: return 0
            negative_count += num < 0

        return 1 if negative_count % 2 == 0 else -1
