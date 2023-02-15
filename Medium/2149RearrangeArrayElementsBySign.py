class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        positive, negative = [], []
        for num in nums:
            if num >= 0:
                positive.append(num)
            else:
                negative.append(num)

        return [num for pair in zip(positive, negative) for num in pair]
