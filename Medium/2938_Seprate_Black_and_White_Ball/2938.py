#URL : https://leetcode.com/problems/separate-black-and-white-balls/description/?envType=daily-question&envId=2024-10-15
#[Medium] [2938] 
#Title: [Seprate Black and White Ball]
#Author: Kartik Bhatnagar
#Date : 2024-10-15 (YYYY-MM-DD)
class Solution:
    def minimumSteps(self, s: str) -> int:
        dis=0
        len_s =len(s)
        tar = len_s-1
        for i in range(len_s-1,-1,-1):
            if s[i]=="1":
                dis += tar - i
                print(i,tar)
                tar -=1
                
        return dis

if __name__ == "__main__":
    s=Solution()
