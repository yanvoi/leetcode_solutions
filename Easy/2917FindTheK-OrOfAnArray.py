class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        bits_set_count = [0] * 31
        for num in nums:
            i = 0
            while num:
                bits_set_count[i] += num & 1
                num >>= 1
                i += 1

        return sum(2 ** i for i, count in enumerate(bits_set_count) if count >= k)
