class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)
        # for i in range(k-1):
        #     heapq.heappop(nums)
        k-=1
        while k!=0:
            k-=1
            heapq.heappop(nums)
        return -nums[0]