class Solution:
    def finalString(self, s: str) -> str:
        answer = collections.deque()
        reverse = False
        for char in s:
            if char == 'i':
                reverse = not reverse
            elif reverse:
                answer.appendleft(char)
            else:
                answer.append(char)

        result = "".join(answer)
        return result[::-1] if reverse else result
