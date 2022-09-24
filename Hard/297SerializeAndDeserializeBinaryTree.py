# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        
        def traverse(node, values):
            if node:
                values.append(str(node.val))
                
                traverse(node.left, values)
                traverse(node.right, values)
            else:
                values.append('#')
        
        values = []
        traverse(root, values)
        return ' '.join(values)

    def deserialize(self, data):
        
        def make_tree(string):
            
            value = string[self.index]
            self.index += 1
            if value == '#':
                return None
            
            root = TreeNode(int(value))
            root.left = make_tree(string)
            root.right = make_tree(string)
            
            return root
        
        # we do not need to check if data is empty
        # because there will always at least be a '#' in the serialize output
        # thus always len(data) != 0
        self.index = 0
        return make_tree(data.split())


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
