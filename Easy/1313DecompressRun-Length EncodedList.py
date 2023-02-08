class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:

        decompressed = []
        for i in range(0, len(nums), 2):
            decompressed += [nums[i+1]] * nums[i]

        return decompressed
