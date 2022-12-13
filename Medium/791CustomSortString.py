class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        # get frequency of every character in s
        s_char_freq = dict()
        for char in s:
            s_char_freq[char] = s_char_freq.get(char, 0) + 1

        answer_arr = []
        # append every character that we know the evaluation of
        for index, char in enumerate(order):
            if char in s_char_freq:
                for _ in range(s_char_freq[char]):
                    answer_arr.append(char)

        evaluated = set(order)
        # append all the other characters
        for char in s_char_freq:
            if char not in evaluated:
                for _ in range(s_char_freq[char]):
                    answer_arr.append(char)

        return ''.join(answer_arr)
