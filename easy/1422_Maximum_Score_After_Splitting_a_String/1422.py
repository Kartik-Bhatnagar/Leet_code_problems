#URL : https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/?envType=daily-question&envId=2025-01-01
#[Easy] [1422] 
#Title: [Maximum Score After Splitting a String]
#Author: Kartik Bhatnagar
#Date : 2025-01-01 (YYYY-MM-DD)

class Solution:
    def maxScore(self, s: str) -> int:
        max_count=0
        for i in range(1,len(s)):
            max_count = max(max_count,s[:i].count("0") + s[i:].count("1"))
        return max_count

if __name__ == "__main__":
    s=Solution()
