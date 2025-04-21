#URL : https://leetcode.com/problems/count-the-hidden-sequences/description/?envType=daily-question&envId=2025-04-21
#[Medium] [2145] 
#Title: [Count the Hidden Sequences]
#Author: Kartik Bhatnagar
#Date : 2025-04-21 (YYYY-MM-DD)
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:         
        cum_max,cum_min = 0,0
        cum_sum = cum_max
        for d in range(0,len(differences)):
            cum_sum = cum_sum +differences[d]
            cum_max = max(cum_sum,cum_max)
            cum_min = min(cum_sum,cum_min)
        # print(cum_max,cum_min)
        lower_range = lower-cum_min
        upper_range = upper -cum_max
        if upper-cum_max < lower - cum_min:return 0
        count = (upper - cum_max) - (lower - cum_min) + 1
        return count
        # print(lower_range,upper_range)
        # return len(range(lower_range,upper_range+1))


        #TLE
        # if lower + differences[0] > upper:
        #     return 0
        # def valid_seq(ele):
        #     for dif in differences:
        #         sm = ele + dif
        #         if not(sm >= lower and sm<=upper):
        #             return False
        #         ele = sm
        #         # print(sm)
        #     return True
        
        # result =0
        # for i in range(lower,upper+1):
        #     # print("**",i)
        #     res =  valid_seq(i)
        #     # print("##",res)
        #     if res:
        #         result+=1
        # return result

        
if __name__ == "__main__":
    s=Solution()
