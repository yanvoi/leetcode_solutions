class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        players = [[score, age] for score, age in zip(scores, ages)]
        players.sort(key=lambda x: (x[1], x[0]))
        dp = [0] * len(players)

        for i in range(len(players)):
            dp[i] = players[i][0]
            for j in range(i):
                if players[j][0] <= players[i][0]:
                    dp[i] = max(dp[i], dp[j] + players[i][0])

        return max(dp)
