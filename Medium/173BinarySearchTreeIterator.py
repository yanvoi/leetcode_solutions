# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    
    # I will have to make it better later
    # so it runs with better memory performance

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.__inorder__(root)
        self.iterator = -1
        

    def next(self) -> int:
        self.iterator += 1
        return self.arr[self.iterator]
        

    def hasNext(self) -> bool:
        return self.iterator < len(self.arr) - 1
        

    def __inorder__(self, node):
        if node:
            self.__inorder__(node.left)
            self.arr.append(node.val)
            self.__inorder__(node.right)
    

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
