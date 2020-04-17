class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans ^= i
        return ans


#        return 2*sum(set(nums))-sum(nums)


#         dic = {}
#         for i in nums:
#             dic[i]=0
#         for i in nums:
#             dic[i]+=1
#         dic = {v:k for k,v in dic.items()}
#         return dic.get(1)
