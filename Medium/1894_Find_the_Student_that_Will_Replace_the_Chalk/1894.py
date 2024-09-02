#URL : https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/?envType=daily-question&envId=2024-09-02
#[Medium] [1894] 
#Title: [Find the Student that Will Replace the Chalk]
#Author: Kartik Bhatnagar
#Date : 2024-09-02 (YYYY-MM-DD)

class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        indx,result=0,0
        full_round_sum = sum(chalk)
        chalk_left = k  % full_round_sum 
        while(chalk_left>=0):
            if chalk_left<chalk[indx]:
                chalk_left =-1
                result = indx
            chalk_left -= chalk[indx]            
            indx+=1
        return result

if __name__ == "__main__":
    s=Solution()
