#URL : https://leetcode.com/problems/first-completely-painted-row-or-column/description/?envType=daily-question&envId=2025-01-20
#[Medium] [2661] 
#Title: [First Completely Painted Row or Column]
#Author: Kartik Bhatnagar
#Date : 2025-01-20 (YYYY-MM-DD)
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        #creating the hash map
        rows,cols = len(mat),len(mat[0])
        mat_pos = {}#n -> (r,c)
        for i in range(rows):
            for j in range(cols):
                mat_pos[mat[i][j]] = (i,j)
        # print(mat_pos)
        row_count = [0]*len(mat)
        col_count = [0]*len(mat[0])
        tot_rows, tot_cols = len(mat), len(mat[0])
        #iterating the array and marking the elements in row_count and col_count wherever  there is a occurance
        #it any row / coulmn touches the max threshold then return the current array postion as the answer
        for i in range(len(arr)):
            r,c  = mat_pos[arr[i]]
            row_count[r] +=1
            col_count[c] +=1
            print(arr[i],r,c, row_count, col_count)
            if row_count[r] == tot_cols:
                return i
            if col_count[c] == tot_rows:
                return i

        
if __name__ == "__main__":
    s=Solution()
