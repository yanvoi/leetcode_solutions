# the inverse of XOR is XOR
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:

        answer = [0] * (len(encoded) + 1)
        answer[0] = first
        for i in range(len(encoded)):
            answer[i + 1] = answer[i] ^ encoded[i]

        return answer
