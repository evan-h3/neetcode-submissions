class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0
        b = len(matrix)-1
        row = None
        #binary search for correct row
        while t<=b:
            mid = (t+b) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif matrix[mid][0] > target:
                b = mid - 1
            elif matrix[mid][0] < target:
                t = mid + 1

        if row == None: return False
        l = 0
        r = len(matrix[row]) - 1
        #find column
        while l<=r:
            mid = (l+r) // 2
            if matrix[row][mid] > target:
                r  = mid - 1
            elif matrix[row][mid] < target:
                l  = mid + 1
            else:
                return True
        
        return False