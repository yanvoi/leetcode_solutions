# we just do what they ask ==> we flip the matrix and sum by rows
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:

        # if the most significant bit is == 0 then we flip the bits in the row
        for row in range(len(grid)):
            if grid[row][0] == 0:
                for col in range(len(grid[0])):
                    grid[row][col] ^= 1

        # check the rest of the bits and for each column try to get as many 1's as possible
        for col in range(1, len(grid[0])):
            count = 0
            for row in range(len(grid)):
                count += grid[row][col]

            if count <= len(grid) // 2:
                for row in range(len(grid)):
                    grid[row][col] ^= 1

        return sum([int(''.join(map(str, row)), 2) for row in grid])
