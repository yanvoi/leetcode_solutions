class Solution:
    def greatestLetter(self, s: str) -> str:

        answer = "0"
        seen = set()
        for char in s:
            seen.add(char)
            if char.isupper() and char.lower() in seen:
                answer = char if ord(char) > ord(answer) else answer
            elif char.islower() and char.upper() in seen:
                answer = char.upper() if ord(char.upper()) > ord(answer) else answer

        return answer if answer != "0" else ""
