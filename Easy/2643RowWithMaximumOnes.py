class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:

        answer = [-1, -1]
        for index, row in enumerate(mat):
            ones_count = row.count(1)
            if ones_count > answer[1]:
                answer = [index, ones_count]

        return answer
