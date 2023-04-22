# clever approach by lee215
# https://leetcode.com/problems/remove-covered-intervals/solutions/451277
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        right, answer = 0, 0
        intervals.sort(key=lambda interval: (interval[0], -interval[1]))

        for i, j in intervals:
            answer += j > right
            right = max(right, j)

        return answer
