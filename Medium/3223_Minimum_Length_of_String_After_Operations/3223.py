#URL : https://leetcode.com/problems/minimum-length-of-string-after-operations/?envType=daily-question&envId=2025-01-10
#[Medium] [3223] 
#Title: [Minimum Length of String After Operations]
#Author: Kartik Bhatnagar
#Date : 2025-01-13 (YYYY-MM-DD)
class Solution:
    def minimumLength(self, s: str) -> int:
        #count each character count
        char_counts = { c: s.count(c) for c in set(s)}
        # print(char_counts)
        surplus =0 #extra characters
        for count in char_counts.values():
            surplus += count//2 if count%2 ==1 else (count//2)-1
        result = len(s) - surplus*2
        return result
if __name__ == "__main__":
    s=Solution()
