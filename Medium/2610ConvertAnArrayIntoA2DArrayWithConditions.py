# O(n) time since we just loop over nums once
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:

        # remember the row index each numbers needs to be added to the next time we see it
        times_seen = defaultdict(int)
        answer = []
        for num in nums:
            # if the result list is too short, we need to make it longer
            if times_seen[num] == len(answer):
                answer.append([])
            answer[times_seen[num]].append(num)
            times_seen[num] += 1

        return answer
