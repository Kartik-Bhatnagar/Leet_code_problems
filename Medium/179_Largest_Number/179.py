#URL : https://leetcode.com/problems/largest-number/description/?envType=daily-question&envId=2024-09-17
#[Medium] [179] 
#Title: [Largest Number]
#Author: Kartik Bhatnagar
#Date : 2024-09-18 (YYYY-MM-DD)
class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        max_num =max(nums)
        if  max_num== 0:
            return "0"
        max_len = len(str(max_num))
        def ones_place(n):
            # n = n + (max_len -len(n))*n[-1]
            print(n,end=" : ")
            n = n*max_len
            print(n)
            return (n)
       
        nums_str = list(map(str,nums))
        #sort the numbers based on ones position
        nums_sort = sorted(nums_str,reverse=True,key = ones_place)
        print(nums_sort)
        return "".join(nums_sort)
if __name__ == "__main__":
    s=Solution()
