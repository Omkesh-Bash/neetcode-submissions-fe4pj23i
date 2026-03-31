class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        mid = 0
        while(mid<=r):
            if r-mid == 1:
                print(nums[mid:r+1])
                return min(nums[mid:r+1])
            mid = (mid+r) // 2
            if nums[mid]<nums[r]:
                r = mid
                mid = 0
            elif nums[mid]>nums[r]:
                pass
            else:
                break
        return nums[r]