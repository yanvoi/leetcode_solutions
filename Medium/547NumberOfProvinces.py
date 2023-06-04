class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        connected_to = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    connected_to[i].append(j)
                    connected_to[j].append(i)

        # perform a BFS starting from each unvisited city
        # incrementing the count of provinces
        provinces_count = 0
        visited = set()
        for city in range(n):
            if city in visited: continue
            provinces_count += 1
            q = collections.deque([city])
            while q:
                cur_city = q.popleft()
                for connected in connected_to[cur_city]:
                    if connected not in visited:
                        q.append(connected)
                        visited.add(connected)

        return provinces_count
