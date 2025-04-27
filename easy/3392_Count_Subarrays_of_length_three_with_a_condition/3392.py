#URL : https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/description/?envType=daily-question&envId=2025-04-26
#[Easy] [3392] 
#Title: [Count Subarrays of length three with a condition]
#Author: Kartik Bhatnagar
#Date : 2025-04-27 (YYYY-MM-DD)
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        if len(nums) <3:
            return 0
        result =0
        for i in range(len(nums)-2):
            arr = nums[i:i+3]
            # print(arr)
            if (arr[0] + arr[2]) == arr[1]/2:
                result+=1
        return result

if __name__ == "__main__":
    s=Solution()
