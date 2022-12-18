class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:

        # for each bit position(32), check the ratio of 1s to 0s
        answer = 0
        for bit_position in range(32):
            count_of_ones = 0
            for num in nums:
                count_of_ones += num>>bit_position & 1

            # count(1) * count(0) will be all the different combinations
            # of pairs with different bits at a certain position
            answer += count_of_ones * (len(nums) - count_of_ones)

        return answer
