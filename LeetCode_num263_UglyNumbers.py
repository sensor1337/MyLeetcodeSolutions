class Solution:
    def isUgly(self, n: int) -> bool:
        for i in 2, 3, 5:
            while n % i == 0:
                n //= i
        return n==1
        if n==0:
            return 0