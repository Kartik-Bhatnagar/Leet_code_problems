#URL : https://leetcode.com/problems/maximum-number-of-points-with-cost/description/?envType=daily-question&envId=2024-08-17
#[Medium] [1937] 
#Title: [Maximum Number of Points with Cost]
#Author: Kartik Bhatnagar
#Date : 2024-08-17 (YYYY-MM-DD)

#Time complexity O(m.n^2) . m->no of rows, n-> no of columns
# Space complexity O(n.m) 
#Solution is accepted but time limit is exceeded
import os
import time
class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        #iterate through each row; for each cell in the row find the max points w.r.t to previous row elements;
        #replace the cell value with the max points it can get through the all elements of previous row
        row_size,col_size = len(points),len(points[0])
        for i in range(1,row_size):
            for j in range(col_size):
                max_cell_dis =0#it stores the max distances of each cell from the previous row
                for pj in range(col_size):
                    max_cell_dis = max(points[i][j] + points[i-1][pj] - abs(j-pj),max_cell_dis)
                points[i][j] = max_cell_dis
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
        print(f"Time taken : {t2-t1} sec")#Time taken : 22.86712622642517
    except Exception as e:
        print(f"fail to run test case\nException {e}")
    print(os.getcwd())
