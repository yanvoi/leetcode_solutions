class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        affects = defaultdict(list)
        for i, (x1, y1, r1) in enumerate(bombs):
            for j, (x2, y2, _) in enumerate(bombs):
                if i != j and sqrt((x1-x2)**2 + (y1-y2)**2) <= r1:
                    affects[i].append(j)

        answer = 0
        for i in range(len(bombs)):
            q = collections.deque([i])
            detonated = set([i])
            while q:
                bomb = q.popleft()
                for bomb_in_range in affects[bomb]:
                    if bomb_in_range not in detonated:
                        detonated.add(bomb_in_range)
                        q.append(bomb_in_range)

            answer = max(answer, len(detonated))

        return answer
