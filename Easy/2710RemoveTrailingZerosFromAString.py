class Solution:
    def removeTrailingZeros(self, num: str) -> str:

        right = len(num) - 1
        while num[right] == "0": right -= 1
        return num[:right+1]
