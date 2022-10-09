# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        
        stack, index = [], 0
        
        while index < len(traversal):
            lvl, val = 0, ''
            
            while index < len(traversal) and traversal[index] == '-':
                lvl += 1
                index += 1
            
            while index < len(traversal) and traversal[index] != '-':
                val += traversal[index]
                index += 1
                
            # if len(stack) > lvl it means that there leafs on the stack
            # so we pop them off of it
            while len(stack) > lvl:
                stack.pop()
                
            node = TreeNode(int(val))
            
            # stack[-1] holds the parent node of the node we just initialized
            if stack and stack[-1].left is None:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
            
            stack.append(node)
            
        return stack[0]
        
