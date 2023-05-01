# O(n) time, O(n) space
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        for asteroid in asteroids:
            # if stack is empty, an asteroid has no other asteroid to collide with yet
            # if an asteroid is going right then we just append it to the stack
            if not stack or asteroid > 0:
                stack.append(asteroid)
                continue
            
            # while an asteroid going left is bigger
            # than asteroids on the stack (going right)
            # pop them from the stack
            while stack and 0 < stack[-1] < -asteroid:
                stack.pop()
            # if asteroid going left has nothing to collide with anymore, append it
            if not stack or (stack and stack[-1] < 0):
                stack.append(asteroid)
            # if they're equally big, destroy both of them
            elif stack and stack[-1] == -asteroid:
                stack.pop()

        return stack
