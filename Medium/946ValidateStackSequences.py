class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        stack = []
        to_pop = 0

        for num in pushed:
            stack.append(num)

            while stack and stack[-1] == popped[to_pop]:
                stack.pop()
                to_pop += 1

        return not stack
