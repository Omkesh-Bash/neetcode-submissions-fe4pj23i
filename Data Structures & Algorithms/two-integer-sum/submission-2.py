class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, element in enumerate(nums):
            e = dict.get(target-element)
            if e is not None:
                return [e, i]
            dict[element] = i