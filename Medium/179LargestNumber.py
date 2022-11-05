class MyEvaluate(str):
    # magic method for implementing > operator
    def __lt__(first, second):
        # comparing 2 concatenations of 2 strings
        # remember that strings are compared differently
        return first+second > second+first


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
            
        ans = sorted(map(str, nums), key=MyEvaluate)
        return ''.join(ans) if ans[0] != '0' else '0'
        
