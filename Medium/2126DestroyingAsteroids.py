class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        for asteroid in sorted(asteroids):
            if asteroid > mass:
                return False
            mass += asteroid

        return True
