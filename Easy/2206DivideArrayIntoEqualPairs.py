class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return all(not count % 2 for count in Counter(nums).values())
