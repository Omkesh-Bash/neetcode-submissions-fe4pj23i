class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = l = 0
        while l<len(nums) :
            s=nums[s]
            l=nums[nums[l]]
            if nums[s] == nums[l]:
                break
        s1 = 0
        while nums[s1] != nums[s]:
            s1 = nums[s1]
            s = nums[s]
        return nums[s1]