# O(n logn) time
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        return sum(sorted(piles)[len(piles) // 3 :: 2])

# same approach but perhaps easier to understand
# class Solution:
#     def maxCoins(self, piles: List[int]) -> int:
#         piles.sort()
#         answer = 0
#         bob, you, alice = 0, len(piles) - 2, len(piles) - 1
#         while bob < you:
#             answer += piles[you]
#             bob += 1
#             you -= 2
#             alice -= 2

#         return answer
