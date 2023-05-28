class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        for char in s:
            if char == "c":
                if not stack or stack.pop() != "b": return False
                if not stack or stack.pop() != "a": return False
            else:
                stack.append(char)

        return not stack
