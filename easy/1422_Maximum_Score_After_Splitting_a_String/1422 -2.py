#URL : https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/?envType=daily-question&envId=2025-01-01
#[Easy] [1422] 
#Title: [Maximum Score After Splitting a String]
#Author: Kartik Bhatnagar
#Date : 2025-01-01 (YYYY-MM-DD)

class Solution:
    def maxScore(self, s: str) -> int:
        zero_count = s[:1].count("0")
        one_count = s[1:].count("1")
        max_count = zero_count + one_count
        # print(max_count)
        for i in range(1,len(s)-1):
            if s[i] == "0":
                zero_count +=1
            else:
                one_count -=1
            max_count = max(max_count, zero_count+one_count)
        return max_count


if __name__ == "__main__":
    s=Solution()
