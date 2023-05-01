# O(n) time, O(n) space
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        for asteroid in asteroids:
            if not stack or asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and 0 < stack[-1] < -asteroid:
                    stack.pop()
                if not stack:
                    stack.append(asteroid)
                elif stack and stack[-1] == -asteroid:
                    stack.pop()
                elif stack and stack[-1] < 0:
                    stack.append(asteroid)

        return stack
