class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        # yet another union find, very tough, need to analyse it again some time

        answer = n = len(vals)
        count = [1] * n
        root = [i for i in range(n)]

        def find(node):
            if node == root[node]:
                return node

            root[node] = find(root[node])
            return root[node]

        edges.sort(key=lambda edge: max(vals[edge[0]], vals[edge[1]]))
        for i, j in edges:
            root1 = find(i)
            root2 = find(j)
            if vals[root1] == vals[root2]:
                answer += count[root1] * count[root2]

                root[root2] = root1
                count[root1] += count[root2]
            elif vals[root1] > vals[root2]:
                root[root2] = root1
            else:
                root[root1] = root2

        return answer
