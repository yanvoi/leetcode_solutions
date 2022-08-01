class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high, row = 0, len(matrix) - 1, -1
        
        while low <= high:
            mid = (low + high) // 2
            
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif target > matrix[mid][-1]:
                low = mid + 1
            else:
                high = mid - 1
                
        if row == -1:
            return False
        
        left, right = 0, len(matrix[row]) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if matrix[row][mid] == target:
                return True
            elif target > matrix[row][mid]:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
        
