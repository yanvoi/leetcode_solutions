# the area of a triangle formed by those points has to be > 0
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1, y1, x2, y2, x3, y3 = points[0][0], points[0][1], points[1][0], points[1][1], points[2][0], points[2][1]
        return x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
