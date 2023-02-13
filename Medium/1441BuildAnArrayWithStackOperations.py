class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        index, answer = 0, []

        for num in range(1, target[-1] + 1):
            answer.append('Push')

            if num == target[index]:
                index += 1
            else:
                answer.append('Pop')

        return answer
