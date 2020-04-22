class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        d = defaultdict(int)
        d[0] = 1
        count = 0
        sums = 0
        for i in nums:
            sums += i
            count += d.get(sums-k,0)
            d[sums] += 1
        return count


        # count = 0
        # for i in range(len(nums)):
        #     sums=0
        #     for j in range(i,len(nums)):
        #         sums = sums + nums[j]
        #         if sums == k:
        #             count+=1
        # return count


        # CUMULATIVE SUM ARRAY
        # count = 0
        # sums = [0] * (len(nums)+1)
        # for i in range(1,len(nums)+1):
        #     sums[i] = sums[i-1] + nums[i-1]
        # print(sums)
        # for i in range(len(nums)+1):
        #     for j in range(i+1,len(nums)+1):
        #         if (sums[j] - sums[i]) == k:
        #             count+=1
        # return count


        # BRUTE FORCE
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         if sum(nums[i:j+1]) == k:
        #             count+=1
        # return count
