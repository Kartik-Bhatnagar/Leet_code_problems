#URL : https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/submissions/1400337827/?envType=daily-question&envId=2024-09-24
#[Medium] [3043] 
#Title: [Find the Length of the Longest Common Prefix]
#Author: Kartik Bhatnagar
#Date : 2024-09-24 (YYYY-MM-DD)
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix_set =set()
        #add arr1 all prefixed in a set
        for num in arr1:
            while(num != 0) and (num not in prefix_set):
                prefix_set.add(num)
                num = num//10
        #iterate through the second list, for each element find the max possible prefix length
        max_res=0
        for num in arr2:
            while (num!=0) and (num not in prefix_set):
                num = num//10
            if num != 0:
                max_res = max(max_res,len(str(num)))
        return max_res
                
if __name__ == "__main__":
    s=Solution()
