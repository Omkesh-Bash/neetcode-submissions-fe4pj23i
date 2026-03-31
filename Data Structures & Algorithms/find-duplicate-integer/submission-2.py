class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = l = 0
        s=nums[s]
        l=nums[nums[l]]
        while nums[s] != nums[l]:
            s=nums[s]
            l=nums[nums[l]]
        s1 = 0
        while nums[s1] != nums[s]:
            s1 = nums[s1]
            s = nums[s]
        return nums[s1]