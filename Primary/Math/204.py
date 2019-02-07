
from math import *

class Solution:
    def __init__(self):
        self.primes = []


    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        for i in range(2, n):
            if self.isPrime(i):
                cnt += 1
        return cnt

    def isPrime(self, num):
        if num < 2:
            return False
        i = 2
        for i in self.primes:
            if num%i == 0:
                return False
        while i**2 < num:
            if num%i == 0:
                return False
            i += 1
        self.primes.append(num)
        return True

s = Solution()

print(s.countPrimes(499))
print(s.primes)


# Java 版本
# 空间复杂度 O(n)
# 时间复杂度 O(n*log(log(n)))
# class Solution {
#     public int countPrimes(int n) {
#        boolean[] isPrime = new boolean[n];
#        for (int i = 2; i < n; i++) {
#           isPrime[i] = true;
#        }
#        // Loop's ending condition is i * i < n instead of i < sqrt(n)
#        // to avoid repeatedly calling an expensive function sqrt().
#        for (int i = 2; i * i < n; i++) {
#           if (!isPrime[i]) continue;
#           for (int j = i * i; j < n; j += i) {
#              isPrime[j] = false;
#           }
#        }
#        int count = 0;
#        for (int i = 2; i < n; i++) {
#           if (isPrime[i]) count++;
#        }
#        return count;
#     }
# }
