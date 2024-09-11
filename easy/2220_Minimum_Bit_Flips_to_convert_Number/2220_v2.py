#URL : https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/?envType=daily-question&envId=2024-09-11
#[Easy] [2220] 
#Title: [Minimum Bit Flips to convert Number]
#Author: Kartik Bhatnagar
#Date : 2024-09-11 (YYYY-MM-DD)
class Solution:
    
    def minBitFlips(self, start: int, goal: int) -> int:
        def dec_to_bin_compare(s,g):
            d=max(s,g)
            if d ==0:
                return 0
            count=0
            while d!=0:
                rem_s = s %2
                rem_g = g %2
                if (rem_s != rem_g):
                    count +=1
                # ans = str(rem)+ans
                d =d//2
                s=s//2
                g=g//2
            return count

        return(dec_to_bin_compare(start,goal))
if __name__ == "__main__":
    s=Solution()
