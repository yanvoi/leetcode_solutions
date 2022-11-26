class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        # O(n) time complexity
        # holds the index of the last occurence of each character
        last_occurence = dict()
        
        for index, char in enumerate(s):
            last_occurence[char] = index
            
        end, ans = 0, []
        for index, char in enumerate(s):
            if end < last_occurence[char]:
                end = last_occurence[char]
                
            if end == index and last_occurence[char] == index:
                ans.append(index + 1)
                
        for i in range(len(ans) - 1, 0, -1):
            ans[i] -= ans[i-1]
            
        return ans
        
