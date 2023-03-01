class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        # just convert nums to a set of decimal numbers
        banned = {int(n, 2) for n in nums}
        digit_count = len(nums[0])

        for number in range(2 ** digit_count):
            if number not in banned:
                in_binary = bin(number)[2:]
                return '0' * (digit_count - len(in_binary)) + in_binary

        return 'error'
