class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        
        # this array will help us determine if a number is prime
        nums = [0] * (n + 1)
        
        # we keep track of the count so we calculate the factorial on the run
        primes_count = 0
        non_primes_count = 1
        
        ans = 1
        
        for i in range(2, len(nums)):
            # if the number is prime
            if nums[i] == 0:
                for j in range(i*i, len(nums), i):
                    nums[j] = 1
                primes_count += 1
                ans = ans * primes_count
            else:
                non_primes_count += 1
                ans = ans * non_primes_count
                    
                    
        return ans % (10**9 + 7)
        
