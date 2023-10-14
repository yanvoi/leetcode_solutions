class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency = Counter(nums)
        return sorted(nums, key=lambda x: (frequency[x], -x))
