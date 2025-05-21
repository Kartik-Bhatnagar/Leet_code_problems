#URL : https://leetcode.com/problems/set-matrix-zeroes/description/?envType=daily-question&envId=2025-05-19
#[Medium] [73] 
#Title: [Set Matrix Zeroes]
#Author: Kartik Bhatnagar
#Date : 2025-05-21 (YYYY-MM-DD)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols = [1 for i in range(len(matrix[0]))] #cols keep track ; if any col has 0 the value will be updated to 0
        rows = [1 for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    cols[j] = 0
                    rows[i] =0
        for i in range(len(matrix)):            
            for j in range(len(matrix[0])):
                if rows[i] == 0 or cols[j] ==0:
                    matrix[i][j] = 0
                



        
if __name__ == "__main__":
    s=Solution()
