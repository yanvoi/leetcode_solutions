class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.__backtrack__(board, i, j, word, 0):
                    return True
                
        return False
    
    def __backtrack__(self, arr, i, j, word, index):
        
        if i < 0 or i >= len(arr) or j < 0 or j >= len(arr[0]): return False
        if arr[i][j] != word[index]: return False
        
        if index == len(word) - 1:
            return True
        
        index += 1
        temporary = arr[i][j]
        arr[i][j] = '#'
            
        up_down = self.__backtrack__(arr, i-1, j, word, index) or self.__backtrack__(arr, i+1, j, word, index)
        left_right = self.__backtrack__(arr, i, j-1, word, index) or self.__backtrack__(arr, i, j+1, word, index)
        
        arr[i][j] = temporary
        return up_down or left_right
        
