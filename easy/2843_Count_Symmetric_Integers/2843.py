#URL : https://leetcode.com/problems/count-symmetric-integers/submissions/1603895783/?envType=daily-question&envId=2025-04-10
#[Easy] [2843] 
#Title: [Count Symmetric Integers]
#Author: Kartik Bhatnagar
#Date : 2025-04-11 (YYYY-MM-DD)
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result =0
        for i in range(low,high+1):
            si =str(i)
            ls = len(si)
            if ls%2 == 0:
                # print(si[:ls//2],si[ls//2:])
                if sum(int(n) for n in (si[:ls//2])) == sum(int(n) for n in (si[ls//2:])):
                    # print("**")
                    result +=1
        return result
                
if __name__ == "__main__":
    s=Solution()
