class Solution:
    def validStrings(self, n: int) -> List[str]:
        result = ["0", "1"]
        for _ in range(n - 1):
            result = ["0" + tail for tail in result] + ["1" + tail for tail in result]

        return [string for string in result if all(a == "1" or b == "1" for a, b in zip(string, string[1:]))]
