#URL : https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/?envType=daily-question&envId=2025-01-07
#[Medium] [1769] 
#Title: [Minimum Number of Operations to Move All Balls to Each Box]
#Author: Kartik Bhatnagar
#Date : 2025-01-07 (YYYY-MM-DD)
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        all_1_indx= [i for i in range(len(boxes)) if boxes[i]=="1"]
        print(all_1_indx)
        result=[]
        for i in range(len(boxes)):
            sm =0
            for j in all_1_indx:
                sm += abs(i-j)
            result.append(sm)
        return result
if __name__ == "__main__":
    s=Solution()
