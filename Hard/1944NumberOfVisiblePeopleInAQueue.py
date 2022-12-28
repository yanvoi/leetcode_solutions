class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:

        output = [0] * len(heights)
        stack = []

        for i in range(len(heights) - 1, -1, -1):
            visible = 0
            while stack and stack[-1] < heights[i]:
                visible += 1
                stack.pop()

            if stack:
                visible += 1

            stack.append(heights[i])
            output[i] = visible

        return output
