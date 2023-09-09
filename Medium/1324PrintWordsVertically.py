class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        longest = max(len(word) for word in words)
        output = []
        for col in range(longest):
            line = []
            for word in range(len(words)):
                char = words[word][col] if col < len(words[word]) else " "
                line.append(char)
            output.append("".join(line).rstrip())

        return output
