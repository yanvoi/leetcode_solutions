class Solution:
    def sumOfThree(self, num: int) -> List[int]:

        # because (x - 1) + x + (x + 1) == num
        x = num // 3
        return [x - 1, x, x + 1] if 3 * x == num else []
