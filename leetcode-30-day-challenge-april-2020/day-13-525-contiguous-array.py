class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # if len(nums)<2:
        #     return 0
        # window = 2
        # ans = 0
        # while window <= len(nums):
        #     for i in range(len(nums)-window+1):
        #         if sum(nums[i:i+window]) == (window/2):
        #             ans = window
        #     window+=2
        # return ans

        if len(nums) < 2:
            return 0
        dict = {0:-1}
        count = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            if count in dict:
                ans = max(ans,i - dict[count])
            else:
                dict[count] = i
        return ans
