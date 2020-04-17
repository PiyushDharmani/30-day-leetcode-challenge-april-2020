class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         left = [0] * n
#         right = [0] * n

#         left[0] = 1
#         right[n-1] = 1

#         for i,j in zip(range(1,n),range(n-2,-1,-1)):
#             left[i] = left[i-1] * nums[i-1]
#             right[j] = nums[j+1] * right[j+1]
#         for i in range(n):
#             nums[i] = left[i] * right[i]

#         return nums
        from functools import reduce
        from operator import mul
        product = reduce(mul,nums)
        print(product)

        return [int(product/i) for i in nums]
