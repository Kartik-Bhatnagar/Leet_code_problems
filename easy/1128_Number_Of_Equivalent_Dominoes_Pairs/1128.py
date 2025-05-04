#URL : https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/?envType=daily-question&envId=2025-05-04
#[Easy] [1128] 
#Title: [Number Of Equivalent Dominoes Pairs]
#Author: Kartik Bhatnagar
#Date : 2025-05-04 (YYYY-MM-DD)
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        all_pairs =dict()
        for i in range(len(dominoes)):
            if dominoes[i][0] <= dominoes[i][1]:
                small = dominoes[i][0]
                big = dominoes[i][1]
            else:
                small  = dominoes[i][1]
                big = dominoes[i][0]
            all_pairs[(small,big)] =  all_pairs.get((small,big),0)+1
        # print(all_pairs)
        result =0
        for v in all_pairs.values():
            if v>1:
                result += (v*(v-1))//2
        return result
        
        #TLE 18/19
        # result =0
        # for i in range(len(dominoes)):
        #     for j in range(i+1,len(dominoes)):
        #         first,second = dominoes[i], dominoes[j]
        #         if first[0]  == second [0] and first[1] == second[1]:
        #             result+=1
        #         elif first[1] == second[0] and first[0] == second[1]:
        #             result+=1
        # return result
                
if __name__ == "__main__":
    s=Solution()
