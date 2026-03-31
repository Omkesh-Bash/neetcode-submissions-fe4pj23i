class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        l, r, q = 0, 0, collections.deque() # stores index

        while r < len(nums):
            # pop all less than rth from right
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if r + 1 >= k:
                output.append(nums[q[0]])
                l +=1
            r+=1
        return output