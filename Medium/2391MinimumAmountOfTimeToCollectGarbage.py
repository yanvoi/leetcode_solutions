class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        answer = 0
        for garbage_type in ['M', 'P', 'G']:
            cur_answer = 0
            for i in range(len(garbage) - 1, -1, -1):
                cur_answer += garbage[i].count(garbage_type)
                if cur_answer and i: cur_answer += travel[i - 1]
            answer += cur_answer

        return answer
