class Solution:
    def mySqrt(self, x: int) -> int:

        for i in range(x+2):
            if i*i <= x:
                continue
            return i-1
        return 0
