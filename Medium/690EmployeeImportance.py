"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        stack, ans = [], 0
        
        h = {e.id: e for e in employees}
        stack.append(h[id])
        
        while stack:
            cur = stack.pop()
            
            ans += cur.importance
            
            for subordinate in cur.subordinates:
                stack.append(h[subordinate])
                
        return ans
        
