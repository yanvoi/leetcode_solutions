# nums consist only of positive integers
# O(n) time, O(1) space
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        greatest, second_greatest = float("-inf"), float("-inf")
        for num in nums:
            if num > greatest:
                greatest, second_greatest = num, greatest
            elif num > second_greatest:
                second_greatest = num

        return (greatest - 1) * (second_greatest - 1)
