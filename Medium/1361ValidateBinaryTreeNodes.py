# O(n) time, O(n) space
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # try to find the root of the tree (if it exists)
        is_a_child = [False] * n
        for node in leftChild + rightChild:
            if node != -1: is_a_child[node] = True
        root = -1
        for node in range(n):
            if not is_a_child[node] and root != -1: return False
            if not is_a_child[node]: root = node
        if root == -1: return False

        # dfs and check if we only visited all nodes once
        visited = [False] * n
        stack = [root]
        while stack:
            node = stack.pop()
            if visited[node]: return False
            visited[node] = True

            if leftChild[node] != -1: stack.append(leftChild[node])
            if rightChild[node] != -1: stack.append(rightChild[node])

        return all(visited)
