class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:

        grouped_by_name = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            # turn HH:MM format to integers representing minutes
            grouped_by_name[name].append(60 * int(time[:2]) + int(time[3:]))

        answer = []
        for name, minutes in grouped_by_name.items():
            times = sorted(minutes)
            for time1, time2 in zip(times, times[2:]):
                if time2 - time1 <= 60:
                    answer.append(name)
                    break

        return sorted(answer)
