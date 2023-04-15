class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:

        self.dp = [[sum(pile[:i]) for i in range(len(pile) + 1)] for pile in piles]
        return self.get_max(0, k)

    
    @cache
    def get_max(self, index, k):
        if not k or index >= len(self.dp):
            return 0

        return max(self.dp[index][i] + self.get_max(index + 1, k - i) 
        for i in range(min(len(self.dp[index]), k + 1)))
