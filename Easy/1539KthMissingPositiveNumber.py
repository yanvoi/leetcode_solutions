# First attempt - time O(n) - space O(1) - not the most efficient but intuitive:
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        answer = k
        for num in arr:
            if num <= answer:
                answer += 1
            else:
                return answer

        return answer
