class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M = len(matrix)
        N = len(matrix[0])

        t, b = 0, M-1
        i = 0
        while t<=b:
            mid = (t+b)//2
            i = mid
            if target < matrix[mid][0]:
                b = mid - 1
            elif target > matrix[mid][0]:
                if t <= matrix[mid][N-1]:
                    break
                t = mid
            else:
                return True
        
        l, r = 0, N-1
        while l<=r:
            mid = (l+r)//2
            if matrix[i][mid] < target:
                l = mid + 1
            elif matrix[i][mid] > target:
                r = mid - 1
            else:
                return True
        
        return False
        
