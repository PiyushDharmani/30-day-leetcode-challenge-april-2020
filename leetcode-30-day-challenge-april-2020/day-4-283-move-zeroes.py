class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # i=0
        # j=0
        # while i < len(nums)-1:
        #     print(i)
        #     if nums[j] == 0:
        #         while nums[i] == 0 and i < len(nums)-1:
        #             i+=1
        #         nums[i],nums[j]=nums[j],nums[i]
        #         j+=1
        #     else:
        #         i+=1
        #         j+=1
        lastNonZero = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[lastNonZero]=nums[lastNonZero],nums[i]
                lastNonZero+=1
