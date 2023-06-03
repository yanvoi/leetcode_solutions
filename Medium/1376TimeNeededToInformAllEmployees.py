class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        is_manager_of = defaultdict(list)
        for i, m in enumerate(manager):
            is_manager_of[m].append(i)

        answer = 0
        stack = [(headID, 0)]
        while stack:
            employee, time = stack.pop()
            if not is_manager_of[employee]:
                answer = max(answer, time)
                continue
            
            takes_time = informTime[employee]
            for subordinate in is_manager_of[employee]:
                stack.append((subordinate, time + takes_time))

        return answer
