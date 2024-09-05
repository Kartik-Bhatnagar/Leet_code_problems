#URL : https://leetcode.com/problems/find-missing-observations/description/?envType=daily-question&envId=2024-09-05
#[Medium] [2028] 
#Title: [Find Missing Observations]
#Author: Kartik Bhatnagar
#Date : 2024-09-05 (YYYY-MM-DD)

class Solution:
    def missingRolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
        l_rolls = len(rolls)
        tot_obs = l_rolls+n
        rem_sum = (mean*tot_obs)-sum(rolls)
        print(rem_sum)
        if rem_sum > (n*6) or rem_sum < n:
            return[]
        result=[]
        rem_ele =n
        for i in range(n):
            d =rem_sum/rem_ele
            ele = int(d)+(d > int(d))
            result.append(ele)
            rem_sum -= ele
            rem_ele -=1
        return result
if __name__ == "__main__":
    s=Solution()
