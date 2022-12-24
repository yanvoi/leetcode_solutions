class Solution:
    def addDigits(self, num: int) -> int:

        while num > 9:
            num = self.__sum_digits__(num)

        return num


    def __sum_digits__(self, num):
        ans = 0
        while num > 0:
            ans += num % 10
            num //= 10

        return ans
