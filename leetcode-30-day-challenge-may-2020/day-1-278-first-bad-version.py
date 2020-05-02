# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        left = 1
        right = n

        while left < right:
            mid = (left+right)//2
            if isBadVersion(mid):
                if isBadVersion(mid-1):
                    right = mid
                else:
                    return mid
            else:
                left = mid + 1

        return left
        
