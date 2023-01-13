class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:

        # READ CAREFULLY WHAT A PATH IS TO UNDERSTAND IT
        self.s = s
        self.answer = 1
        self.children = defaultdict(list)
        for child_node, parent_node in enumerate(parent):
            self.children[parent_node].append(child_node)

        self.dfs(0)
        return self.answer


    def dfs(self, node):
        
        longest, second_longest = 0, 0
        for child in self.children[node]:
            going_down = self.dfs(child)
            if self.s[node] == self.s[child]: continue

            if going_down > longest:
                longest, second_longest = going_down, longest
            elif going_down > second_longest:
                second_longest = going_down

        # the path is either gonna be the current node + it's both children
        # or we pass the longest straight path to the parent of the current node
        self.answer = max(self.answer, longest + second_longest + 1)
        return longest + 1
        
