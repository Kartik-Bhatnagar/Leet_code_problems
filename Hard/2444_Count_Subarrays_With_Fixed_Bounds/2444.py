#URL : https://leetcode.com/problems/count-subarrays-with-fixed-bounds/description/?envType=daily-question&envId=2025-04-26
#[Hard] [2444] 
#Title: [Count Subarrays With Fixed Bounds]
#Author: Kartik Bhatnagar
#Date : 2025-04-26 (YYYY-MM-DD)
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        start=mini=maxi=-1
        result =0
        #start will hold the latest encountered outofrange index(beyond minK to maxK)
        for i in range(len(nums)):
            if nums[i] < minK or nums[i]>maxK:
                start = i
            if nums[i] == minK:
                mini = i
            if nums[i] ==maxK:
                maxi = i
            result += max(0,min(mini,maxi) - start)
        return result
        #_______Brute Force _TLE_______37/53
        # def isFixedBounSarray(arr):
        #     if max(arr) == maxK and min(arr) ==minK:
        #         return True
        #     return False
        # result = 0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)+1):
        #         # print(nums[i:j],result)
        #         if isFixedBounSarray(nums[i:j]):
                    
        #             result +=1
        # return result
        
if __name__ == "__main__":
    s=Solution()
