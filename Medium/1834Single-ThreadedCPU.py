# use minimum heap to retrieve the shortest available task
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        order = []
        tasks_sorted = sorted((enq, process, i) for i, (enq, process) in enumerate(tasks))
        heap = []
        i, cur_time = 0, 0

        while len(order) < len(tasks):
            while i < len(tasks) and tasks_sorted[i][0] <= cur_time:
                heapq.heappush(heap, (tasks_sorted[i][1], tasks_sorted[i][2]))
                i += 1

            if heap:
                exec_time, task_index = heapq.heappop(heap)
                cur_time += exec_time
                order.append(task_index)
            elif i < len(tasks):
                cur_time = tasks_sorted[i][0]

        return order
