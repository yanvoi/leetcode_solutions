"""
You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.
Return the minimum number of cameras needed to monitor all nodes of the tree.
 
Example 1:
Input: root = [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.

Example 2:
Input: root = [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.

 
Constraints:

	The number of nodes in the tree is in the range [1, 1000].
	Node.val == 0

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(n) time, O(n) space, dfs
# null node ==> 0
# leaf node ==> 1
# node with a camera ==> 2
# node with a child with a camera ==> 0
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.answer = 0
        return (self.dfs(root) == 1) + self.answer

    
    def dfs(self, node):
        if not node:
            return 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)
        # this node is a leaf (can be monitored by its parent - like a leaf)
        if left == 0 and right == 0:
            return 1
        # this node has a non-monitored child (set up a camera)
        if left == 1 or right == 1:
            self.answer += 1
            return 2

        # this node has a child with a camera (no need to set up a camera)
        # works like a non-existent node
        return 0
