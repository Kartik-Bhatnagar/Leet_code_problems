#URL : https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/?envType=daily-question&envId=2024-09-11
#[Easy] [2220] 
#Title: [Minimum Bit Flips to convert Number]
#Author: Kartik Bhatnagar
#Date : 2024-09-11 (YYYY-MM-DD)
class Solution:
    
    def minBitFlips(self, start: int, goal: int) -> int:
        def dec_to_bin(d):
            if d ==0:
                return "0"
            ans=""
            while d!=0:
                rem = d %2
                ans = str(rem)+ans
                d =d//2
            return ans
        def prefix_0(s,g):
            mlen= max(len(s),len(g))
            #append 0 for those binary number having len than m len
            if len(s) < mlen:
                count_0 = mlen-len(s)
                s ="0"*count_0 +s
            if len(g) <mlen:
                g ="0"*(mlen-len(g))+g
            return s,g
        def compare_bin(s,g):
            #returns the number of unmatched string postion in s and g
            count=0
            for i in range(len(s)):
                if s[i]!=g[i]:
                    count+=1
            return count

        st =dec_to_bin(start)
        go =(dec_to_bin(goal))
        # print(st,go)
        # print(prefix_0(st,go))
        st,go=prefix_0(st,go)
        return compare_bin(st,go)
        

if __name__ == "__main__":
    s=Solution()
