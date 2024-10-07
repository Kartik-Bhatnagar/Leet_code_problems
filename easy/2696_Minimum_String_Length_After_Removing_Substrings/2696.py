#URL : https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/?envType=daily-question&envId=2024-10-07
#[Easy] [2696] 
#Title: [Minimum String Length After Removing Substrings]
#Author: Kartik Bhatnagar
#Date : 2024-10-07 (YYYY-MM-DD)
class Solution:
    def minLength(self, s: str) -> int:
        ab_stat,cd_stat = True,True
        while ab_stat or cd_stat:
            ab_stat,cd_stat = True,True
            if "AB" not in s:
                ab_stat = False
            else:
                s = "".join(s.split("AB"))
            if "CD" not in s:
                cd_stat = False
            else:
                s = "".join(s.split("CD"))
        return len(s)
if __name__ == "__main__":
    s=Solution()
