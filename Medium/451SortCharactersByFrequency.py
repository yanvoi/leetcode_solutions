class Solution:
    def frequencySort(self, s: str) -> str:
        
        freq = dict()
        for char in s:
            freq[char] = freq.get(char, 0) + 1
            
        reverse_freq = dict()
        chars = set(s)
        for char in chars:
            reverse_freq[freq[char]] = reverse_freq.get(freq[char], []) + [char]
            
        ans = []
        for length in range(len(s), 0, -1):
            if length in reverse_freq:
                for char in reverse_freq[length]:
                    ans = ans + [char] * length
        
        return ''.join(ans)
        
