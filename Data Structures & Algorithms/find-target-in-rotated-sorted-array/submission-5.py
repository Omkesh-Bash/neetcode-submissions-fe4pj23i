class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while(l <= r):
            mid = (l+r) // 2
            if(nums[mid] == target):
                return mid
            elif(nums[l] <= nums[r]):
                if(nums[mid] < target):
                    l = mid+1
                elif(nums[mid] > target): #
                    r = mid-1

            elif(nums[mid] > target and target < nums[l] and nums[l] > nums[mid]):
                r = mid-1
                if(nums[r] == target):
                    return r
            elif(nums[mid] > target and target < nums[l]):
                l = mid+1
            elif(nums[mid] > target and target >= nums[l] and nums[l] < nums[mid]) :
                r = mid-1
            elif(nums[mid] > target and target >= nums[l]) :
                l = mid+1
            elif(nums[mid] < target and target >= nums[l] and nums[l] < nums[mid]):
                l = mid+1
            elif(nums[mid] < target and target >= nums[l]):
                r = mid-1
            elif(nums[mid] < target and target < nums[l]):
                #   1  3                    3       5
#                   6   2                   2       3
    #               2    1                   1      5
    #               5    1                   1      5
    #               5    2                   3      5
    #               5    2                   2      5
    #               5    3                   3      3
    #               7    8                   8      4

                l = mid+1
        return -1