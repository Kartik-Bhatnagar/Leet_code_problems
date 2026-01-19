#URL : https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/
#[Medium] [1292] 
#Title: [Maximum Side Length of a Square with Sum Less than or Equal to Threshold]
#Author: Kartik Bhatnagar
#Date : 2026-01-19 (YYYY-MM-DD)
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        #credits: https://www.youtube.com/watch?v=olDXKOSydpg
        row_grid =[]#[[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(len(mat)):
            prev=0
            row_lis=[]
            for j in range(len(mat[0])):
                cm_val = prev + mat[i][j]
                row_lis.append(cm_val)
                prev = cm_val
            row_grid.append(row_lis)
        # print(row_grid)
        #we will start our iteration from the largest possible square length and will iterate till length 1. if anywhere between we find the square with sum less than threshold then we will immediate terminate and return the answer 
        #NOte: len 1 square is itself a magic square
        row_len = len(mat)
        col_len = len(mat[0])
        sq_len = min(col_len,row_len)
        
        while(sq_len>=0):
            # print(f"SQ LEN {sq_len}")
            for i in range(0,(row_len-sq_len)+1):
                for j in range(0,(col_len-sq_len)+1):
                    row_sum =0                    
                    for r in range(i,i+sq_len):
                        row_sum += row_grid[r][j+sq_len-1] - (row_grid[r][j-1] if j-1 >= 0 else 0)
                    #check if all coumns sum is equal to target
                    if row_sum <= threshold:
                        return sq_len
                    
            sq_len-=1
        return -1
if __name__ == "__main__":
    s=Solution()
