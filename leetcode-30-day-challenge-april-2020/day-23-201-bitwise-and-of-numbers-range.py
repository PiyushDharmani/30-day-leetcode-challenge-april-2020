class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # find and remove LSB while its in range
        while m < n:
            n -= (n & -n)
        return n

        #BRUTE FORCE SOLUTION
        # ans = m
        # for i in range(m+1,n+1):
        #     ans &= i
        # return ans
        
