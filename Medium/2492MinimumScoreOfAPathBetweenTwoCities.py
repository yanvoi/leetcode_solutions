class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        adj = defaultdict(dict)
        for a, b, distance in roads:
            adj[a][b] = adj[b][a] = distance

        q = collections.deque([1])
        seen = set()
        answer = float('inf')

        while q:
            node = q.popleft()
            for neighbor, distance in adj[node].items():
                answer = min(answer, distance)
                if neighbor not in seen:
                    q.append(neighbor)
                    seen.add(neighbor)

        return answer
