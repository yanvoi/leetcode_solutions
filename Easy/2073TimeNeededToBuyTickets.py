# O(n) time: long one-liner but a one-liner nonetheless
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        return sum(min(num, tickets[k]) for num in tickets[:k]) + tickets[k] + sum(min(num, tickets[k] - 1) for num in tickets[k + 1:])
