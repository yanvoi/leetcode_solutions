class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        # O(n) time complexity
        # indices: left most and right most occurence in the string
        lr_occurence = dict()
        
        for index, char in enumerate(s):
            if char in lr_occurence:
                lr_occurence[char][1] = index
            else:
                lr_occurence[char] = [index, index]
            
        end, ans = 0, []
        for index, char in enumerate(s):
            if index >= end and lr_occurence[char][0] == lr_occurence[char][1]:
                ans.append(index + 1)
            elif lr_occurence[char][1] > end:
                end = lr_occurence[char][1]
            elif lr_occurence[char][1] <= end and index == end:
                ans.append(end + 1)
                
        for i in range(len(ans) - 1, 0, -1):
            ans[i] -= ans[i-1]
            
        return ans
        
