class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1]
        count = [0] * len(primes)
        
        while n > 1:
            
            mini, minis = float('inf'), []
            for i in range(len(primes)):
                if primes[i] * ugly[count[i]] < mini:
                    minis = []
                    mini = primes[i] * ugly[count[i]]
                    minis.append(i)
                elif primes[i] * ugly[count[i]] == mini:
                    minis.append(i)
                    
            for index in minis:
                count[index] += 1
                
            ugly.append(mini)
            n -= 1
        
        return ugly[-1]
    
