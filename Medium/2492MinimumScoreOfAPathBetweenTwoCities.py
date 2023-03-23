class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        adj = defaultdict(list)
        for a, b, distance in roads:
            adj[a].append([b, distance])
            adj[b].append([a, distance])

        q = collections.deque([1])
        answer = float('inf')
        seen = set()

        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                seen.add(node)
                for neighbor, distance in adj[node]:
                    answer = min(answer, distance)
                    if neighbor not in seen:
                        q.append(neighbor)

        return answer
