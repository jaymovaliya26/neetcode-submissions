class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0,rows-1
        while top<=bottom:
            midRow = top + (bottom-top)//2
            if target > matrix[midRow][-1]:
                top=midRow+1
            elif target < matrix[midRow][0]:
                bottom = midRow-1
            else:
                break

        if not (top<=bottom):
            return False

        row = top + (bottom-top)//2
        l,r = 0,cols-1
        while l<=r:
            m = l+(r-l)//2
            if target>matrix[row][m]:
                l=m+1
            elif target< matrix[row][m]:
                r=m-1
            else:
                return True
        
        return False