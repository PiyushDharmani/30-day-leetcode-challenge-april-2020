class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # ans = max(nums)
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         ans = max(ans,sum(nums[i:j+1]))
        # return ans

        max_current = nums[0]
        max_global = nums[0]
        for i in range(1,len(nums)):
            max_current = max(nums[i],nums[i]+max_current)
            if max_current > max_global:
                max_global = max_current
        return max_global
