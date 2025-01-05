#URL : https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/?envType=problem-list-v2&envId=ajgq0zjc
#[Medium] [1930] 
#Title: [ Unique Length-3 Palindromic Subsequences]
#Author: Kartik Bhatnagar
#Date : 2025-01-05 (YYYY-MM-DD)
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        if len(s)<3:
            return 0
        pali =set()
        s_len = len(s)
        chars_indx = { c:[s.index(c),(s_len-s[::-1].index(c))-1] for c in set(s)} #first and last index of the character
        result =0
        for c in chars_indx:
            result+= len(set(s[chars_indx[c][0]+1:chars_indx[c][1]]))
        return result

if __name__ == "__main__":
    s=Solution()
