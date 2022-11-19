# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        q = collections.deque()
        if root:
            q.append(root)
        ans = 0
            
        while q:
            lvl_size, level = len(q), []
            
            for _ in range(lvl_size):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                
            ans += self.__min_swaps__(level)
            
        return ans
        
        
    def __min_swaps__(self, arr):
        
        ans = 0
        indices = dict()
        for i, val in enumerate(arr):
            indices[val] = i
        
        temp = sorted(arr)
        
        for i in range(len(arr)):
            if arr[i] != temp[i]:
                
                ans += 1
                moved_val = arr[i]
                moved_after_index = indices[temp[i]]
                
                arr[i], arr[indices[temp[i]]] = arr[indices[temp[i]]], arr[i]
                
                indices[moved_val] = moved_after_index
                
        return ans
    
