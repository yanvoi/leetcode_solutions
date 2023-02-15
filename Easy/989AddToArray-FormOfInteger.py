class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        for i in range(len(num) - 1, -1, -1):
            k += num[i]
            num[i] = k % 10
            k //= 10

        return [int(digit) for digit in str(k)] + num if k > 0 else num
