#URL : https://leetcode.com/problems/pascals-triangle/description/?envType=daily-question&envId=2025-08-01
#[Easy] [118] 
#Title: [Pascal's Triangle]
#Author: Kartik Bhatnagar
#Date : 2025-08-01 (YYYY-MM-DD)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result =[[1]]
        prev_row=[1]
        for r in range(1, numRows):
            row =[1]
            for i in range(1,len(prev_row)):
                row.append(prev_row[i-1]+prev_row[i])
            row.append(1)
            result.append(row)
            prev_row = row
            # print(row)
        return result
            
        
if __name__ == "__main__":
    s=Solution()
