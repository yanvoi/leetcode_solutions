# consider how many times each number will be included in an odd length subarray
# it depends on it's position
# O(n) time, O(1) space
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        return sum(num * (((i + 1) * (len(arr) - i) + 1) // 2) for i, num in enumerate(arr))
