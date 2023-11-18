# brilliant solution by lee215 making it O(nlogn) time
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        answer, satisfactions_so_far = 0, 0
        for num in sorted(satisfaction, reverse=True):
            if satisfactions_so_far + num <= 0: break
            satisfactions_so_far += num
            answer += satisfactions_so_far

        return answer


# what I came up with initially - O(n^2) time, O(1) space
# class Solution:
#     def maxSatisfaction(self, satisfaction: List[int]) -> int:
#         satisfaction.sort()
#         answer = 0
#         for index in range(len(satisfaction)):
#             answer = max(answer, sum((i + 1) * num for i, num in enumerate(satisfaction[index:])))

#         return answer
