class Solution:

    def is_inside(self, point, circle):
        x, y = point
        i, j, r = circle

        return math.dist([x, y], [i, j]) <= r

    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        answer = []
        for circle in queries:
            count = 0
            for point in points:
                if self.is_inside(point, circle):
                    count += 1

            answer.append(count)

        return answer
