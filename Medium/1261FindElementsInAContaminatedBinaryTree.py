# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        
        root.val = 0
        q = collections.deque()
        q.append(root)
        self.available = set()
        
        while q:
            
            q_size = len(q)
            for _ in range(q_size):
                node = q.popleft()
                self.available.add(node.val)
                
                if node.left:
                    node.left.val = 2 * node.val + 1
                    q.append(node.left)
                if node.right:
                    node.right.val = 2 * node.val + 2
                    q.append(node.right)
                

    def find(self, target: int) -> bool:
        return target in self.available
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
