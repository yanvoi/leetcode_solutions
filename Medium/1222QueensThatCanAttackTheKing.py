class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        
        # very simple
        # very fast
        # but very long code
        attackers = set([tuple(x) for x in queens])
        king_row, king_col = king[0], king[1]
        ans = []
        
        i = king_row - 1
        while i >= 0:
            if (i, king_col) in attackers:
                ans.append([i, king_col])
                break
            i -= 1
                
        i = king_row + 1
        while i < 8:
            if (i, king_col) in attackers:
                ans.append([i, king_col])
                break
            i += 1
        
        j = king_col - 1
        while j >= 0:
            if (king_row, j) in attackers:
                ans.append([king_row, j])
                break
            j -= 1
        
        j = king_col + 1
        while j < 8:
            if (king_row, j) in attackers:
                ans.append([king_row, j])
                break
            j += 1
            
        i, j = king_row - 1, king_col - 1
        while i >= 0 and j >= 0:
            if (i, j) in attackers:
                ans.append([i, j])
                break
            i -= 1
            j -= 1
            
        i, j = king_row - 1, king_col + 1
        while i >= 0 and j < 8:
            if (i, j) in attackers:
                ans.append([i, j])
                break
            i -= 1
            j += 1
            
        i, j = king_row + 1, king_col - 1
        while i < 8 and j >= 0:
            if (i, j) in attackers:
                ans.append([i, j])
                break
            i += 1
            j -= 1
        
        i, j = king_row + 1, king_col + 1
        while i < 8 and j < 8:
            if (i, j) in attackers:
                ans.append([i, j])
                break
            i += 1
            j += 1
            
        return ans
        
