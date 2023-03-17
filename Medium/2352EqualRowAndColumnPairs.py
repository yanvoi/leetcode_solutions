class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        count_row = Counter(tuple(row) for row in grid)
        count_col = defaultdict(int)
        for col in range(len(grid[0])):
            column = []
            for row in range(len(grid)):
                column.append(grid[row][col])
            count_col[tuple(column)] += 1

        return sum(c1 * c2 for key1, c1 in count_row.items() for key2, c2 in count_col.items() if key1 == key2)
