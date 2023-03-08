class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left, right = 1, max(piles)

        while left < right:
            k = (left + right) // 2

            # if we spend too much time eating the bananas
            if sum(math.ceil(pile / k) for pile in piles) > h:
                left = k + 1
            else:
                right = k

        return left
