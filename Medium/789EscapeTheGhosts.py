# simply check if all ghosts are further away from the target than you
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:

        x, y = target
        our_distance = abs(x) + abs(y)
        return all(abs(x - i) + abs(y - j) > our_distance for i, j in ghosts)
