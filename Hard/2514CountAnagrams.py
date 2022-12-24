# for each word in the string
# we count the number of unique permutations of characters in this word
# and return the product of the result

class Solution:
    def countAnagrams(self, s: str) -> int:
        
        answer = 1
        for word in s.split():
            answer *= self.count_unique_permutations(word)
            
        return answer % (10**9 + 7)
    
    
    def count_unique_permutations(self, s):
        answer = math.factorial(len(s))
        
        freq = dict()
        for char in s:
            freq[char] = freq.get(char, 0) + 1
            
        for num in freq.values():
            answer //= math.factorial(num)
            
        return answer
        
