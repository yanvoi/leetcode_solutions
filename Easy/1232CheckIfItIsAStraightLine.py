class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        x1, y1 = coordinates.pop()
        x2, y2 = coordinates.pop()

        for x3, y3 in coordinates:
            triangle_area = x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)
            # if the area of a triangle made by any 3 given points is > 0
            if triangle_area:
                return False

        return True
