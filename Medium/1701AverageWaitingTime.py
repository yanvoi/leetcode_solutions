class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:

        waiting_times = []
        cur_time = 0
        for arrival, time in customers:
            if cur_time < arrival:
                waiting_times.append(time)
                cur_time = arrival + time
            else:
                to_wait = time + (cur_time - arrival)
                waiting_times.append(to_wait)
                cur_time = arrival + to_wait

        return sum(waiting_times) / len(waiting_times)
