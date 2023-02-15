# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# turn the tree into a grap using DFS and then do simple BFS from the target node
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        self.adj = defaultdict(set)
        self.connect(root)
        queue = [target.val]
        visited = set()

        for _ in range(k):
            next_queue = []
            for node in queue:
                for neighb in self.adj[node]:
                    if neighb not in visited: next_queue.append(neighb)

            visited |= set(queue)
            queue = next_queue

        return queue

    
    def connect(self, root):

        if root.left:
            self.adj[root.val].add(root.left.val)
            self.adj[root.left.val].add(root.val)
            self.connect(root.left)

        if root.right:
            self.adj[root.val].add(root.right.val)
            self.adj[root.right.val].add(root.val)
            self.connect(root.right)
