class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        leads_to = defaultdict(list)
        incoming = defaultdict(list)
        for a, b in connections:
            leads_to[a].append(b)
            incoming[b].append(a)

        q = collections.deque([0])
        visited = set([0])
        answer = 0

        while q:
            city = q.popleft()
            for adj in leads_to[city]:
                if adj not in visited:
                    answer += 1
                    visited.add(adj)
                    q.append(adj)
            for adj in incoming[city]:
                if adj not in visited:
                    visited.add(adj)
                    q.append(adj)

        return answer
