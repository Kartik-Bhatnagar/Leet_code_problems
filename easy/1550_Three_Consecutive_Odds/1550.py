#URL : https://leetcode.com/problems/three-consecutive-odds/description/?envType=daily-question&envId=2025-05-11
#[Easy] [1550] 
#Title: [Three Consecutive Odds]
#Author: Kartik Bhatnagar
#Date : 2025-05-11 (YYYY-MM-DD)
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd_count = 0
        for num in arr:
            if num %2 == 1:
                odd_count +=1
            else :
                odd_count =0
            # print(f" {num} : {odd_count}")
            if odd_count == 3:
                return True
        return False
        
if __name__ == "__main__":
    s=Solution()
