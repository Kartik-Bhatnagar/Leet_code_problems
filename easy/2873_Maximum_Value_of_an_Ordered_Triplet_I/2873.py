#URL : https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/submissions/1594674272/?envType=daily-question&envId=2025-04-02
#[Easy] [2873] 
#Title: [Maximum Value of an Ordered Triplet I]
#Author: Kartik Bhatnagar
#Date : 2025-04-02 (YYYY-MM-DD)
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        num_len = len(nums)
        max_val = 0
        for i in range(0,num_len):
            for j in range(i+1,num_len):
                for k in range(j+1,num_len):
                    # print(i,j,k)
                    max_val = max(max_val,(nums[i]-nums[j])*nums[k])
        return max_val

        

if __name__ == "__main__":
    s=Solution()
