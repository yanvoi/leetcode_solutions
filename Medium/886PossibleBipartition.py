class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        adjacent = dict()
        for first, second in dislikes:
            adjacent[first] = adjacent.get(first, []) + [second]
            adjacent[second] = adjacent.get(second, []) + [first]

        assigned_group = dict()
        q = collections.deque()

        for person in range(1, n+1):
            if person in assigned_group: continue

            # True means group A, False means group B
            assigned_group[person] = True
            q.append((person, True))

            while q:
                cur_person, cur_group = q.popleft()
                if cur_person not in adjacent: continue
                
                for adj in adjacent[cur_person]:
                    if adj in assigned_group and assigned_group[adj] == cur_group:
                        return False
                    if adj not in assigned_group:
                        assigned_group[adj] = not cur_group
                        q.append((adj, not cur_group))

        return True
