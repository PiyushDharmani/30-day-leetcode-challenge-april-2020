# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # use binary search to find starting index of 1 in each row and return minimum index
        startindex = float('inf')
        n, m = BinaryMatrix.dimensions(binaryMatrix)
        for row in range(n):
            left = 0
            right = n-1
            while left <= right:
                mid = (left+right)//2
                if  BinaryMatrix.get(binaryMatrix,row,mid) == 1:
                    startindex = min(startindex,mid)
                    right = mid - 1
                else:
                    left = mid + 1
        if startindex == float('inf'):
            return -1
        return startindex
