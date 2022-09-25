# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        
        def traverse(node, arr):
            if node:
                arr.append(str(node.val))
                
                traverse(node.left, arr)
                traverse(node.right, arr)
            else:
                arr.append('#')
        
        ret = []
        traverse(root, ret)
        return ' '.join(ret)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        def __deserialize__(string):
            value = string[self.index]
            self.index += 1
            
            if value == '#':
                return None
            
            root = TreeNode(int(value))
            root.left = __deserialize__(string)
            root.right = __deserialize__(string)
            
            return root
        
        self.index = 0
        return __deserialize__(data.split())
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
