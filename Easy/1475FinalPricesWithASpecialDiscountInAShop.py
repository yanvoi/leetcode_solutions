# I was sure that it could be solved in O(n) using stack
# but I had to check other people's solutions
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        stack = []
        for i, cur_price in enumerate(prices):
            while stack and cur_price <= prices[stack[-1]]:
                prices[stack.pop()] -= cur_price
            stack.append(i)

        return prices
