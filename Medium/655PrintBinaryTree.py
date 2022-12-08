# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:

        height = self.__get_height__(root)
        # [(2^height) - 1] because it is the sum of all nodes in a perfect binary tree of height h-1
        self.answer = [['' for _ in range((2 ** height) - 1)] for i in range(height)]
        
        self.__traverse__(root, 0, 0, len(self.answer[0])-1)
        return self.answer

    
    def __get_height__(self, root):

        if not root:
            return 0

        return 1 + max(self.__get_height__(root.left), self.__get_height__(root.right))

    def __traverse__(self, node, row, left, right):

        if not node:
            return

        mid = (left + right) // 2
        self.answer[row][mid] = str(node.val)
        self.__traverse__(node.left, row+1, left, mid-1)
        self.__traverse__(node.right, row+1, mid+1, right)
        
