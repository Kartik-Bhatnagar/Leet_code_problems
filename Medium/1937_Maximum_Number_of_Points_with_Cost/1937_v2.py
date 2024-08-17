#URL : https://leetcode.com/problems/maximum-number-of-points-with-cost/description/?envType=daily-question&envId=2024-08-17
#[Medium] [1937] 
#Title: [Maximum Number of Points with Cost]
#Author: Kartik Bhatnagar
#Date : 2024-08-17 (YYYY-MM-DD)

#V2:
#time taken on sample problem is reduce from 22 sec to 1.4 sec
#Time complexity went down from O(m.n^2) to O(m.2n). m->no of rows, n-> no of columns
# Space complexity O(n.m) 

#V2: on each cell we will create two list from the previous cell(left and right) 
#left row : each cell will contain max point it can get among all left cells to the current cell
#right row : each cell will contain max point it can get among all right cells to the current cell
#in this way for each cell we don't need to iterate all cell of previous row to find the max_point, we can just lookup from right and left list

import time
class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        #iterate through each row; for each cell in the row find the max points w.r.t to previous row elements;
        #replace the cell value with the max points it can get through the all elements of previous row
        row_size,col_size = len(points),len(points[0])
        for i in range(1,row_size):

            left,right=[0 for i in range(col_size)],[0 for i in range(col_size)]
            left[0] = points[i-1][0]
            for l in range(1,col_size):
                left[l] = max(left[l-1]-1,points[i-1][l])
            right[col_size-1] = points[i-1][col_size-1]
            for r in range(col_size-2,-1,-1):
                right[r]= max(right[r+1]-1,points[i-1][r])
            print(left,right)
            for j in range(col_size):
                max_cell_dis =max(left[j],right[j]) + points[i][j]#it stores the max distances of each cell from the previous row
                points[i][j] = max_cell_dis
            # print(points[j])
        print(points)
        return max(points[-1])

if __name__ == "__main__":
    s=Solution()
    points = [[1,2,3],[1,5,1],[3,1,1]]
    print(s.maxPoints(points))
    points = [[1,5],[2,3],[4,2]]
    print(s.maxPoints(points))
    try:
        with open ("./data/tc_140.txt","r")as d:
            points = eval(d.read())
            # print(points[:100])
        t1= time.time()
        print(s.maxPoints(points))#108657
        t2=time.time()
        print(f"Time taken : {t2-t1} sec")#Time taken : 1.390063762664795 sec
    except Exception as e:
        print(f"fail to run test case\nException {e}")

