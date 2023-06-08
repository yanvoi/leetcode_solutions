class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        def my_bisect(arr, val):
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] >= val:
                    left = mid + 1
                else:
                    right = mid
            
            return left

        count = 0
        n = len(grid[0])
        for row in grid:
            count += n - my_bisect(row, 0)

        return count
