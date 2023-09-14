# O(n) time, O(1) space, 3 passes, one liner :)
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        return moves.count("_") + abs(moves.count("L") - moves.count("R"))

# O(n) time, O(1) space, single pass
# class Solution:
#     def furthestDistanceFromOrigin(self, moves: str) -> int:
#         relative, absolute = 0, 0
#         for move in moves:
#             if move == "R": relative += 1
#             elif move == "L": relative -= 1
#             else: absolute += 1

#         return absolute + abs(relative)
