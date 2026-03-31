class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i, element in enumerate(nums):
            i2 = dict1.get(target-element)
            if(i2 is not None):

                return [i2, i]
            dict1[element] = i