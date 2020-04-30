class Solution:
    def canJump(self, nums: List[int]) -> bool:

        lastPos = len(nums) - 1
        start = len(nums) - 1

        while start >=0:
            if (start + nums[start]) >= lastPos:
                lastPos = start
            start-=1

        return lastPos == 0

        # from functools import lru_cache
        # @lru_cache()
        # def helper(position):
        #     if position == len(nums) - 1:
        #         return True
        #     farthestPosition = min(position + nums[position],len(nums) - 1)
        #     start = position + 1
        #     while farthestPosition >= start:
        #         if helper(farthestPosition):
        #             return True
        #         farthestPosition -= 1
        #     return False
        # return helper(0)
        
