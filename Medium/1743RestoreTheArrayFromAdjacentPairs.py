class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        adj = defaultdict(list)
        for u, v in adjacentPairs:
            adj[u].append(v)
            adj[v].append(u)

        outermost = [num for num, a in adj.items() if len(a) == 1]
        answer = []
        cur, prev = outermost[0], outermost[0]

        for _ in range(len(adj)):
            answer.append(cur)

            # take into account the edge case of the last element
            candidates = [val for val in adj[cur] if val != prev]
            cur, prev = candidates[0] if candidates else None, cur

        return answer
