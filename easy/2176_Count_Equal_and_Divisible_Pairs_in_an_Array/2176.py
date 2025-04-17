#URL : https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/submissions/1609623725/?envType=daily-question&envId=2025-04-17
#[Easy] [2176] 
#Title: [Count Equal and Divisible Pairs in an Array]
#Author: Kartik Bhatnagar
#Date : 2025-04-17 (YYYY-MM-DD)
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        result=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                # print(i,j)
                if (nums[i] == nums[j]):
                    if (i*j)%k == 0:
                        result+=1
        return result
if __name__ == "__main__":
    s=Solution()
