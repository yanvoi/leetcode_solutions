class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        freq, most_frequent = dict(), 0
        for word in words:
            freq[word] = freq.get(word, 0) + 1
            most_frequent = max(most_frequent, freq[word])
            
        ans = []
        for i in range(most_frequent, 0, -1):
            cur = [key for key, val in freq.items() if val == i]
            cur.sort()
            ans += cur
            
            if len(ans) >= k:
                return ans[:k]
        
        return ans
        
