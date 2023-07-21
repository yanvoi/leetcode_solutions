class Solution:
    def interpret(self, command: str) -> str:
        index = 0
        answer = []
        while index < len(command):
            if command[index] == "G":
                answer.append("G")
                index += 1
            elif command[index:index+2] == "()":
                answer.append("o")
                index += 2
            else:
                answer.append("al")
                index += 4

        return "".join(answer)
