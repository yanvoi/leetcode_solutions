class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        answer = [0] * len(A)
        seen = prefix = 0
        for i, pair in enumerate(zip(A, B)):
            for num in pair:
                if (1 << num) & seen:
                    prefix += 1
                seen |= (1 << num)

            answer[i] = prefix

        return answer
