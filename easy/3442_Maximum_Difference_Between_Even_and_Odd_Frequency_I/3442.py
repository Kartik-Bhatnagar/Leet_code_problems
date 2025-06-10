#URL : https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/description/?envType=daily-question&envId=2025-06-05
#[Easy] [3442] 
#Title: [Maximum Difference Between Even and Odd Frequency I]
#Author: Kartik Bhatnagar
#Date : 2025-06-10 (YYYY-MM-DD)
class Solution:
    def maxDifference(self, s: str) -> int:
        d =dict()
        max_odd =0
        min_even = 100
        for c in s:
            d[c] = d.get(c,0)+1
        for k,v in d.items():
            if v%2 == 0: #even
                min_even = min(min_even,v)
            else: #odd
                max_odd = max(max_odd,v)
        # print(d)
        # if max_odd <max_even:
        #     return max_odd - min_even
        return (max_odd-min_even)
        print(d)
        

if __name__ == "__main__":
    s=Solution()
