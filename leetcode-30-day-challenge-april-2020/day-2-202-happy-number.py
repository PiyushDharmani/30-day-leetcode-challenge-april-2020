import math
class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        def squareSum(number):
            num = list(str(number))
            su = 0
            for n in num:
                su+= int(n)**2
            return su
        s = set()
        while True:
            n = squareSum(n)
            if n in s:
                return False
            else:
                if n==1:
                    return True
                s.add(n)
