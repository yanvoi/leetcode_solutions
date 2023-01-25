class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        self.edges = edges
        visited1, visited2 = [False] * len(edges), [False] * len(edges)
        distance1, distance2 = [-1] * len(edges), [-1] * len(edges)

        self.dfs(node1, visited1, distance1)
        self.dfs(node2, visited2, distance2)

        answer = -1
        min_distance = float('inf')
        for node in range(len(edges)):
            if visited1[node] and visited2[node] and min_distance > max(distance1[node], distance2[node]):
                min_distance = max(distance1[node], distance2[node])
                answer = node

        return answer


    def dfs(self, node, visited, distance):

        visited[node] = True
        leads_to = self.edges[node]

        if leads_to == -1 or visited[leads_to]:
            return

        distance[leads_to] = distance[node] + 1
        self.dfs(leads_to, visited, distance)
