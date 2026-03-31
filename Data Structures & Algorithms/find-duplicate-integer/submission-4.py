class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = f = 0
        s=nums[s]
        f=nums[nums[f]]
        while s != f:
            s=nums[s]
            f=nums[nums[f]]
        s1 = 0
        while s1 != s:
            s1 = nums[s1]
            s = nums[s]
        return s1
            
        