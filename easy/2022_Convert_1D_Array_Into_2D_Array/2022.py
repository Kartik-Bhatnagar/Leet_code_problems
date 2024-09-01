#URL : https://leetcode.com/problems/convert-1d-array-into-2d-array/?envType=daily-question&envId=2024-09-01
#[Easy] [2022] 
#Title: [Convert 1D Array Into 2D Array]
#Author: Kartik Bhatnagar
#Date : 2024-09-01 (YYYY-MM-DD)
class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        result=[]
        if (m*n)!= len(original):
            return result
        prev= 0
        result = [original[n*(i-1):(n*i)] for i in range(1,m+1) ]
        # for i in range(1,m+1):
        #     result.append(original[prev:(n*i)])
        #     prev= (n*i)
        return result
if __name__ == "__main__":
    s=Solution()
