#URL : https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/?envType=daily-question&envId=2025-03-12
#[Easy] [2529] 
#Title: [Maximum Count of Positive Integer and Negative Integer]
#Author: Kartik Bhatnagar
#Date : 2025-03-12 (YYYY-MM-DD)
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg_count,count =0,0
        for num in nums:
            if num <0:
                neg_count +=1
            elif num>0:
                break
            count +=1
        return (max(neg_count,len(nums)-count))
if __name__ == "__main__":
    s=Solution()
