class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # initialize needed variables
        n = len(nums)
        left, right = [1] * n, [1] * n 
        product_array = []
        
        # left array holds product of numbers left to each number in the array
        # right array holds product of numbers right to each number in the array
        
        # fill out the left array
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
        
        # fill out the right array
        for i in range(n - 2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
            
        # for each number multiply products of numbers to left and right
        for i in range(n):
            product_array.append(left[i] * right[i])
            
        return product_array
        
