class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        total = len(A) + len(B)
        half = total//2
        l, r  = 0, len(A)-1
        while True:
            i = (l+r) // 2
            j = half-i-2        # one for i and one for half, because indexing starts form 0, so -2
            ALeft = A[i] if i >= 0 else float("-infinity")
            ARight = A[i+1] if i+1 < len(A) else float("infinity")
            BLeft =  B[j] if j >= 0 else float("-infinity")
            BRight = B[j+1] if j+1 < len(B) else float("infinity")

            if ALeft <= BRight and BLeft <= ARight:
                if total%2: # odd
                    return min(ARight, BRight)
                return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
            elif ALeft > BRight:
                r = i-1
            else :
                l = i+1