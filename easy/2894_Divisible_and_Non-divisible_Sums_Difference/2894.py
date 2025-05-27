#URL : https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/description/
#[Easy] [2894] 
#Title: [Divisible and Non-divisible Sums Difference]
#Author: Kartik Bhatnagar
#Date : 2025-05-27 (YYYY-MM-DD)
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # tot_sm = ((n)*(n+1)/2)#sum of first n numbers
        non_div_sm = 0
        div_sm = 0
        for i in range(1,n+1):
            if i % m != 0:
                non_div_sm += i
            else:
                div_sm +=i
        return non_div_sm - div_sm

if __name__ == "__main__":
    s=Solution()
