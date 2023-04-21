class Solution:
    def numTeams(self, rating: List[int]) -> int:

        greater_count = [0] * len(rating)
        less_count = [0] * len(rating)
        for i in range(len(rating)):
            for j in range(i + 1, len(rating)):
                if rating[i] < rating[j]:
                    greater_count[i] += 1
                else:
                    less_count[i] += 1

        answer = 0
        for i in range(len(rating)):
            for j in range(i + 1, len(rating)):
                if rating[i] < rating[j]:
                    answer += greater_count[j]
                elif rating[i] > rating[j]:
                    answer += less_count[j]

        return answer
