class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r,c  = len(matrix), len(matrix[0])
        row_track = [0]*r
        col_track = [0]*c

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    row_track[i] = -1
                    col_track[j] = -1

        for i in range(r):
            for j in range(c):
                if row_track[i] == -1 or col_track[j] == -1:
                    matrix[i][j] = 0
        
