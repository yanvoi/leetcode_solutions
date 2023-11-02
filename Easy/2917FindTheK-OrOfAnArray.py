class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        count = Counter()
        for num in nums:
            i = 0
            while num:
                count[i] += num & 1
                num >>= 1
                i += 1

        return sum(2 ** key for key, val in count.items() if val >= k)
