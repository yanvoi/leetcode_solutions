class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return " ".join(word.lower() if len(word) < 3 else word[0].upper() + word[1:].lower() for word in title.split())
