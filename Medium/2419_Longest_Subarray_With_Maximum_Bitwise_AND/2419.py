#URL : https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/?envType=daily-question&envId=2024-09-14
#[Medium] [2419] 
#Title: [Longest Subarray With Maximum Bitwise AND]
#Author: Kartik Bhatnagar
#Date : 2024-09-14 (YYYY-MM-DD)

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mnum = max(nums)
        #the maximum possible bitwise AND is only possible with the maximum element 
        #no matter how many subarry we align the maximum possible bitwise AND is possible with the maximum element in the list
        first_indx= nums.index(mnum)
        max_count = 0
        cur_count=0
        for num in nums:
            if num == mnum:
                cur_count +=1
                max_count = max(cur_count,max_count)
            else:
                cur_count =0
        return max_count
        
if __name__ == "__main__":
    s=Solution()
