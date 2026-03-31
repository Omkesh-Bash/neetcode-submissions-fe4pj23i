class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix)-1
        while(top <= bot):
            row = (top+bot) // 2
            if(matrix[row][0] > target):
                bot = row - 1
            elif(matrix[row][-1] < target):
                top = row + 1
            else:
                break
        if (top > bot):
            return False
        l, h = 0, len(matrix[0])
        while(l <= h):
            mid = (l+h) // 2
            if(matrix[row][mid] < target):
                l = mid + 1
            elif matrix[row][mid] > target:
                h = mid - 1
            else:
                return True
        return False