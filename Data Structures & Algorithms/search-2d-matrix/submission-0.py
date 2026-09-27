class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we pefomr binary search on the first elemetnns of the rows, the check is to see if the number falls in the range, then we do binary search on that part
        l, r = 0, len(matrix) -1
        while l <= r:
            m = (r+l) // 2
            if matrix[m][0] <= target <= matrix[m][len(matrix[m])-1]:
                # do bin search again
                ll, rr = 0, len(matrix[m])
                while ll <= rr:
                    mm = (rr+ll) // 2
                    if matrix[m][mm] == target:
                        return True
                    elif target < matrix[m][mm]:
                        rr = mm-1
                    else:
                        ll = mm+1
                break
            elif target < matrix[m][0]:
                r = m-1
            else:
                l = m+1
        return False