class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        leads_to = defaultdict(list)
        for u, v, w in times:
            leads_to[u].append((v, w))

        q = collections.deque()
        # the queue will hold node numbers and the time it took to reach them
        q.append((k, 0))
        time_to_reach = [0] + [inf] * n

        while q:
            node, time = q.popleft()
            if time < time_to_reach[node]:
                time_to_reach[node] = time
                for target, cost in leads_to[node]:
                    q.append((target, time + cost))

        answer = max(time_to_reach)
        return answer if answer < inf else -1
