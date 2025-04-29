#URL : https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/?source=submission-noac
#[Medium] [2962] 
#Title: [Count Subarrays Where Max Element Appears at Least K Times]
#Author: Kartik Bhatnagar
#Date : 2025-04-29 (YYYY-MM-DD)
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_n = max(nums)        
        indx_max =[]
        for i in range(len(nums)):
            if nums[i] == max_n:
                indx_max.append(i)
        print(indx_max)
        if len(indx_max) < k:
            return 0
        left_indx=0
        right_indx=k-1
        result =0
        nums_len  = len(nums)
        for i in range(len(nums)):
            # print(f"{i}  {left_indx}  {right_indx}")
            # print(f"**{nums[indx_max[left_indx]:indx_max[right_indx-1]]}")
            if i <= indx_max[left_indx]:
                result += nums_len - indx_max[right_indx]
                
            else :
                left_indx += 1
                if  right_indx+1< len(indx_max):
                    right_indx +=1
                    result += nums_len -indx_max[right_indx]
                else:
                    break
            # print(f"{i} #{result} //{ nums_len} __{indx_max[right_indx]}")
        
        return result

        # max_n = max(nums)
        # result = 0
        # cnt=0
        # for left in range(len(nums)):
        #     cnt=0
        #     for right in range(left+1,len(nums)+1):
        #         if nums[right-1] == max_n:
        #             cnt +=1
        #         # print(f"{nums[left:right]} __ {left} , {right}, {cnt}")
        #         if cnt == k:
        #             result += len(nums)-right+1
        #             break
                
        # return result
        #two pointer__forward appraoch __TLE __622/633
        # max_n = max(nums)
        # result = 0
        # for left in range(len(nums)):
        #     right = left+k
        #     cnt = nums[left:right].count(max_n)
        #     # print(f"** {nums[left:right]}")
        #     if cnt >= k:
        #         result += len(nums) - right+1
        #         continue
        #     for right in range(left+k+1,len(nums)+1):
        #         # print(f"{nums[left:right]} __ {left} , {right}, {cnt}")
        #         if nums[right-1] == max_n:
        #             cnt+=1
        #         if cnt == k:
        #             result += len(nums)-right+1
        #             break
                
        # return result

if __name__ == "__main__":
    s=Solution()
