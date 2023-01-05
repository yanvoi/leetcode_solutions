class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        # sort by the end of each balloon because we will pop the end greedily
        # trying to burts as many baloons overlapping with the last one
        points.sort(key=lambda x: x[1])
        arrow_count, last_end = 0, 0

        for start, end in points:
            if arrow_count == 0 or start > last_end:
                arrow_count += 1
                last_end = end

        return arrow_count
