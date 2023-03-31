# group the indices of 'connected' characters and sort these groups

class UnionFind:
    def __init__(self, n):
        self.head = [i for i in range(n)]

    def union(self, i, j):
        self.head[self.find(j)] = self.find(i)

    def find(self, i):
        if i != self.head[i]:
            self.head[i] = self.find(self.head[i])
        return self.head[i]


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        uf, char_groups = UnionFind(len(s)), defaultdict(list)

        for a, b in pairs:
            uf.union(a, b)

        for i, char in enumerate(s):
            char_groups[uf.find(i)].append(char)
            
        for key, chars in list(char_groups.items()):
            char_groups[key] = sorted(chars, reverse=True)

        return ''.join([char_groups[uf.find(i)].pop() for i in range(len(s))])
