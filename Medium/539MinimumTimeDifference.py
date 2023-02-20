# O(n)
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        # mark all present minutes as True
        time_present = [False] * 24 * 60
        for point in timePoints:
            minute = 60 * int(point[:2]) + int(point[3:])
            # if a certain clock time point has already been seen we can return 0
            if time_present[minute]:
                return 0
            time_present[minute] = True

        # get the minimum difference between any two indices holding True
        # loop over the list twice since time is "circular"
        n = len(time_present)
        prev_index, answer = float('-inf'), float('inf')
        for cur_index in range(n * 2):
            if time_present[cur_index % n]:
                answer = min(answer, cur_index - prev_index)
                prev_index = cur_index

        return answer
