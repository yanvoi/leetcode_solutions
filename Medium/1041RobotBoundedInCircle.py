class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, directions, cur_dir = 0, 0, [(0, 1), (1, 0), (0, -1), (-1, 0)], 0
        for instruction in instructions:
            if instruction == "R":
                cur_dir = (cur_dir + 1) % 4
            elif instruction == "L":
                cur_dir = (cur_dir - 1) % 4
            else:
                i, j = directions[cur_dir]
                x, y = x + i, y + j

        return (x, y) == (0, 0) or cur_dir != 0
