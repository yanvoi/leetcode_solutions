class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        bars_count = 0
        coins_left = coins

        for cost in sorted(costs):
            if cost <= coins_left:
                coins_left -= cost
                bars_count += 1

        return bars_count
