class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # definition of atan2: https://en.wikipedia.org/wiki/Atan2
        # we count the number of vectors with the same atan2

        if len(points) == 1: return 1

        answer = 2
        for i in range(len(points)):
            count = defaultdict(int)
            x1, y1 = points[i]
            for j in range(len(points)):
                if j == i: continue
                x2, y2 = points[j]

                count[math.atan2(y2 - y1, x2 - x1)] += 1

            answer = max(answer, max(count.values()) + 1)

        return answer
        
