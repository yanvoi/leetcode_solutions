# standard BFS
# count the number of nodes in separate subgraphs
# this will allow us to calculate the answer
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        nodes = n
        answer = 0

        for i in range(n):
            if i in visited: continue

            q = collections.deque([i])
            count = 0
            while q:
                node = q.popleft()
                visited.add(node)
                count += 1
                for neighbor in adj[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)

            nodes -= count
            answer += count * nodes

        return answer
