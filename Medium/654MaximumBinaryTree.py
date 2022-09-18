# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        if len(nums) == 0: return None
        
        biggest = self.__find_max__(nums)
        
        root = TreeNode(nums[biggest])
        root.left = self.constructMaximumBinaryTree(nums[:biggest])
        root.right = self.constructMaximumBinaryTree(nums[biggest+1:])
        
        return root
        
    def __find_max__(self, nums):
        biggest = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[biggest]:
                biggest = i
                
        return biggest
    
