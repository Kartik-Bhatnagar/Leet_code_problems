#URL : https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/submissions/1600826251/?envType=daily-question&envId=2025-04-08
#[Easy] [3396] 
#Title: [Minimum Number of Operations to Make Elements in Array Distinct]
#Author: Kartik Bhatnagar
#Date : 2025-04-08 (YYYY-MM-DD)
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums_t = nums
        result =0
        while len(nums_t) >0 :
            if len(set(nums_t)) == len(nums_t):
                break
            if len(nums_t) >= 3:    
                nums_t = nums_t[3:]
                result +=1
            else:
                result +=1
                break
        return result

        
if __name__ == "__main__":
    s=Solution()
