class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        votes_sum = defaultdict(int)
        leader = -1
        self.winner_by_time = []

        for person in persons:
            votes_sum[person] += 1
            if votes_sum[person] >= votes_sum[leader]:
                leader = person
            
            self.winner_by_time.append(leader)

    def q(self, t: int) -> int:
        index = bisect.bisect(self.times, t)
        return self.winner_by_time[index - 1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
