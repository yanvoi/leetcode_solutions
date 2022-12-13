class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # simple binary search for each row
        for row in matrix:

            left, right = 0, len(row) - 1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] == target:
                    return True

                if target > row[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False
        
