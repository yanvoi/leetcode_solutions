class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count = 0
        frequency = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                count += frequency[nums[i] * nums[j]]
                frequency[nums[i] * nums[j]] += 1

        return 8 * count
