import math
from typing import List

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # Helper function to check if a number is prime
        def isPrime(n):
            if n <= 1:
                return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True
        
        # Generate a list of primes
        primes = []
        for i in range(1, 1000 + 1):
            if isPrime(i):
                primes.append(i)

        # Binary search to find primes less than x
        def binarySearch(x):
            l, r = 0, len(primes) - 1
            while l <= r:
                mid = (l + r) // 2
                if primes[mid] == x:
                    return primes[:mid]  # Return primes less than x
                elif primes[mid] < x:
                    l = mid + 1
                else:
                    r = mid - 1
            return primes[:r + 1]  # Return primes less than x
        
        prev = float('-inf')  # Track the previous number to ensure valid operation
        for num in nums:
            largestPrime = binarySearch(num)
            canContinue = False

            # Try to reduce num using primes in reverse order
            for prime in reversed(largestPrime):
                if prev < num - prime and num - prime != 0:
                    prev = num - prime
                    canContinue = True
                    break
            
            # If no valid reduction was found, check the condition
            if not canContinue:
                if not (prev < num):
                    return False
                prev = num

        return True
