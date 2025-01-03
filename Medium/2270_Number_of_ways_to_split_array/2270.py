#URL : https://leetcode.com/problems/number-of-ways-to-split-array/?envType=daily-question&envId=2025-01-03
#[Medium] [2270] 
#Title: [Number of ways to split array]
#Author: Kartik Bhatnagar
#Date : 2025-01-03 (YYYY-MM-DD)
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # Keep track of sum of elements on left and right sides
        whole_right_sum = sum(nums)
        whole_left_sum =0
        result =0
        for i in range(0,len(nums)-1):
            whole_right_sum -= nums[i]
            whole_left_sum += nums[i]
            # print(f"{whole_right_sum}  {whole_left_sum}")
            if whole_left_sum >= whole_right_sum :
                result+=1
        return result

if __name__ == "__main__":
    s=Solution()
