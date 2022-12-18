class Solution:
    def optimalDivision(self, nums: List[int]) -> str:

        ans = [str(nums[0])]
        # edge cases
        if len(nums) == 1:
            return ''.join(ans)
        if len(nums) == 2:
            return ''.join(ans) + f'/{str(nums[1])}'

        # the optimal solution always follows the same pattern
        # we make the divisor of the first number as small as possible
        ans += [f'/({str(nums[1])}']
        for i in range(2, len(nums)):
            ans += [f'/{str(nums[i])}']

        ans += [')']
        return ''.join(ans)
