"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

# read carefully what a Quad Tree is and the problem becomes very easy - keep on dividing the grid
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        # edge cases
        if not grid: return None
        if self.is_leaf(grid): return Node(grid[0][0], True, None, None, None, None)

        # get all children of a node
        # a parent node is basically just a link to it's children - it doesn't represent a part of a grid
        n = len(grid)
        top_left = self.construct([sub_grid[:n//2] for sub_grid in grid[:n//2]])
        top_right = self.construct([sub_grid[n//2:] for sub_grid in grid[:n//2]])
        bottom_left = self.construct([sub_grid[:n//2] for sub_grid in grid[n//2:]])
        bottom_right = self.construct([sub_grid[n//2:] for sub_grid in grid[n//2:]])

        return Node('parent', False, top_left, top_right, bottom_left, bottom_right)


    def is_leaf(self, sub_grid):

        # we always divide the grids into squares
        # if a grid is univalent then the node representing it will be a leaf
        n = len(sub_grid)
        return all(sub_grid[0][0] == sub_grid[i][j] for i in range(n) for j in range(n))
        
