# O(n) time, O(1) space
# remember how many positions back you have seen 1 last time
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_seen = float("inf")
        for num in nums:
            if num and last_seen < k: return False
            if num: last_seen = 0
            else: last_seen += 1

        return True
