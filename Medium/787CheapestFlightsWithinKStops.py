class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        directions = defaultdict(list)
        for from_i, to_i, price_i in flights:
            directions[from_i].append([to_i, price_i])

        dist = [float('inf')] * n
        stops = 0
        q = deque()
        q.append([src, 0])

        while q and stops <= k:
            cur_size = len(q)
            for _ in range(cur_size):
                node, cur_price = q.popleft()

                for adj, price in directions[node]:
                    if cur_price + price >= dist[adj]:
                        continue

                    dist[adj] = cur_price + price
                    q.append([adj, dist[adj]])

            stops += 1

        return dist[dst] if dist[dst] != float('inf') else -1
