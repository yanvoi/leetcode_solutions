class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        red, blue = defaultdict(set), defaultdict(set)

        for a, b in redEdges:
            red[a].add(b)
        for u, v in blueEdges:
            blue[u].add(v)

        queue = deque([(0, True), (0, False)])
        cur_dist = 0
        distance = [float('inf')] * n

        while queue:
            size = len(queue)
            for _ in range(size):
                node, color = queue.popleft()

                distance[node] = min(distance[node], cur_dist)
                if color:
                    for adj in list(red[node]):
                        queue.append((adj, not color))
                        red[node].remove(adj)
                else:
                    for adj in list(blue[node]):
                        queue.append((adj, not color))
                        blue[node].remove(adj)

            cur_dist += 1

        return [d if d != float('inf') else -1 for d in distance]
