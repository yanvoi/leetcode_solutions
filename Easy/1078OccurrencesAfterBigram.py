class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:

        formatted_text = text.split()
        third = []
        for f, s, t in zip(formatted_text, formatted_text[1:], formatted_text[2:]):
            if f == first and s == second:
                third.append(t)

        return third
