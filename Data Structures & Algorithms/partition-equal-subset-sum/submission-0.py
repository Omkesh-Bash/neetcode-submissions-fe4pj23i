class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = {0,}
        _sum = sum(nums)
        if _sum % 2 != 0:
            return False
        half = _sum/2
        for n in nums:
            cpy = s.copy()
            for i in s:
                res = i + n
                if res == half:
                    return True
                cpy.add(res)
            s = cpy
        return False