class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        count = collections.Counter(nums)
        points = [num * count[num] for num in range(max(count.keys()) + 1)]
        
        # same as in the house robber problem - we can't take from two adjacent fields
        prev, cur = 0, 0
        for num in points:
            prev, cur = cur, max(cur, prev + num)

        return cur
