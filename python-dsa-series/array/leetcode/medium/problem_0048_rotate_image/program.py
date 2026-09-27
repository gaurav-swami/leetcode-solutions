class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def rev_row(row: list[int]) -> None:
            l,r = 0,len(row)-1
            while l<r:
                row[l],row[r] = row[r], row[l]
                l+=1
                r-=1

        n = len(matrix)
    
        for i in range(n):
            for j in range(i+1,n):
                matrix[j][i], matrix[i][j] = matrix[i][j],matrix[j][i]

        for row in matrix:
            rev_row(row)


#time complexity  = O(n*n) + O(n*n) = O(2n^2) = O(n^2)
#space complexity = O(n)
