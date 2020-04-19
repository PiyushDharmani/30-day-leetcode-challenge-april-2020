class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while (l < r):
            mid = l + (r-l)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        rl = l
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            realMid = (mid+rl)%len(nums)

            if nums[realMid] == target:
                return realMid

            elif nums[realMid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1
