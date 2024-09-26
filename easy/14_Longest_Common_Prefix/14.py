#URL : https://leetcode.com/problems/longest-common-prefix/description/
#[Easy] [14] 
#Title: [Longest Common Prefix]
#Author: Kartik Bhatnagar
#Date : 2024-09-24 (YYYY-MM-DD)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in range(1,len(strs)):
            temp =""
            for i in range(0,min(len(prefix),len(strs[s]))):
                if strs[s][i] == prefix[i]:
                    temp += prefix[i]
                else:
                    break
            prefix = temp
        return prefix
if __name__ == "__main__":
    s=Solution()
