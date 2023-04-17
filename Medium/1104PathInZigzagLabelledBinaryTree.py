class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:

        level, lvl = 1, 1
        while label >= lvl * 2:
            level += 1
            lvl *= 2

        nodes = []
        while level:
            nodes.append(label)
            left, right = (2 ** (level - 1)), 2 ** level - 1
            parent = (right - (label - left)) // 2
            label = parent
            level -= 1

        return nodes[::-1]
