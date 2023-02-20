# O(n)
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        # mark all present minutes as True
        time_present = [False] * 24 * 60
        for point in timePoints:
            time = 60 * int(point[:2]) + int(point[3:])
            if time_present[time]:
                return 0
            time_present[time] = True

        # get the minimum difference between any two indices holding True
        prev, answer, n = float('-inf'), float('inf'), len(time_present)
        for i in range(n * 2):
            if time_present[i % n]:
                answer = min(answer, i - prev)
                prev = i

        return answer
