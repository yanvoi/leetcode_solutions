# O(n) time, O(n) space
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor = [num for num in nums]
        for i in range(1, len(xor)):
            xor[i] ^= xor[i - 1]

        maximum = (2 ** maximumBit) - 1
        return [maximum ^ xor[-i - 1] for i, num in enumerate(nums)]
