# this is a standard finding convex hull problem but done clever
# amazing solution by chaudhary1337:
# https://leetcode.com/problems/erect-the-fence/solutions/1442266/a-detailed-explanation-with-diagrams-graham-scan/
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:

        def cross_product(t1, t2, t3):
            x1, y1 = t1
            x2, y2 = t2
            x3, y3 = t3

            return (y3-y2)*(x2-x1) - (y2-y1)*(x3-x2)
        

        points = sorted(trees)
        # it's handy to separate the stack into 2 stacks because of the possible angles
        lower, upper = [], []

        for point in points:
            while len(lower) >= 2 and cross_product(lower[-2], lower[-1], point) < 0:
                lower.pop()
            while len(upper) >= 2 and cross_product(upper[-2], upper[-1], point) > 0:
                upper.pop()

            lower.append(point)
            upper.append(point)

        return list({tuple(p) for p in lower} | {tuple(p) for p in upper})
