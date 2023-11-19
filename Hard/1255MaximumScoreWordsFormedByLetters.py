class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        self.words, self.score = words, score
        count = [0] * len(score)
        for letter in letters:
            count[ord(letter) - ord('a')] += 1

        return self.backtrack(count, 0)

    def backtrack(self, count, index):
        answer = 0
        for i in range(index, len(self.words)):
            cur_result = 0
            can_make_the_word = True
            for char in self.words[i]:
                cur_result += self.score[ord(char) - ord('a')]
                count[ord(char) - ord('a')] -= 1
                if count[ord(char) - ord('a')] < 0: can_make_the_word = False

            if can_make_the_word:
                cur_result += self.backtrack(count, i + 1)
                answer = max(answer, cur_result)

            for char in self.words[i]:
                count[ord(char) - ord('a')] += 1
        
        return answer
