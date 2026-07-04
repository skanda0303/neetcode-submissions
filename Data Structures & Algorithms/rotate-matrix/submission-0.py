class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(len(matrix)):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(len(matrix)):
            start = 0
            end = len(matrix)-1
            while start < end:
                matrix[i][start],matrix[i][end] = matrix[i][end],matrix[i][start]
                start+=1
                end -=1
        
        
