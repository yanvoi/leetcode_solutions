class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:

        minutes_active = defaultdict(set)
        for user_id, minute in logs:
            minutes_active[user_id].add(minute)

        answer = [0] * k
        for minutes in minutes_active.values():
            answer[len(minutes)-1] += 1

        return answer
