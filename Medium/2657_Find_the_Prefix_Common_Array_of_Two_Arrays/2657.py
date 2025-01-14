#URL : https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/?envType=daily-question&envId=2025-01-10
#[Medium] [2657] 
#Title: [Find the Prefix Common Array of Two Arrays]
#Author: Kartik Bhatnagar
#Date : 2025-01-14 (YYYY-MM-DD)
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        common =[]
        result =[]
        cur_count =0
        for i in range(len(A)):
            if A[i] in common:
                cur_count +=1
            common.append(A[i])
            if B[i] in common:
                cur_count +=1
            common.append(B[i])
            result.append(cur_count)
        return result
if __name__ == "__main__":
    s=Solution()
