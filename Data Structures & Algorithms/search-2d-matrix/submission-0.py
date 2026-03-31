class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numRows, numColumns = len(matrix), len(matrix[0])
        low , high = 0, numRows-1
        while(low <= high):
            mid = (low + high) // 2
            if(matrix[mid][0] == target):
                return True
            elif(matrix[mid][0] < target):
                low = mid + 1
            else:
                high = mid - 1
        low = 1
        high = numColumns-1
        if(matrix[mid][0] > target):
            mid-=1
        # print(mid)
        while low<=high:
            mid2 = (low + high) // 2
            if(matrix[mid][mid2] == target):
                return True
            elif(matrix[mid][mid2] < target):
                low = mid2 + 1
            else:
                high = mid2 - 1
        return False