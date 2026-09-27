class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        rows,cols = len(matrix),len(matrix[0])
        n = rows*cols
        result = []
                                      
        r,c = 0,-1
        d = 1     #direction
      
        while len(result)<n: 
            for i in range(cols):
                c+=d   
                result.append(matrix[r][c])
            for j in range(rows-1):
                r+=d
                result.append(matrix[r][c])
            
            d *= -1
            rows -= 1 #shrinking dimensions
            cols -= 1
                          
        return result


#time complexity - O(n*m)
#space complexity - O(n*m)
