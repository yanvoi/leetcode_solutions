class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:

        x_coordinates = sorted([x for x, y in points])
        return max([j - i for i, j in zip(x_coordinates, x_coordinates[1:])] + [0])
