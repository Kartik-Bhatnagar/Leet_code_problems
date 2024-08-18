#URL : https://leetcode.com/problems/ugly-number-ii/?envType=daily-question&envId=2024-08-18
#[Medium] [264] 
#Title: [Ugly Number II]
#Author: Kartik Bhatnagar
#Date : 2024-08-18 (YYYY-MM-DD)
import time
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        count=1
        valid_num=[2,3,5]
        num = 2
        discard =[]
        while(count<n):            
            # print(num,count)
            if 0 in [num%d for d in discard]:
                # print("{",num)
                pass
            elif 0 in [num%pnm for pnm in valid_num] :                
                count+=1
                
            else :
                discard.append(num)
            print("%",num,count)
            num+=1

             
        return num-1   

if __name__ == "__main__":
    s=Solution()
    n=11
    print(s.nthUglyNumber(n))
    n=1
    print(s.nthUglyNumber(n))
    t1= time.time()
    n=201
    # print(s.nthUglyNumber(n))
    t2=time.time()
    # print(f"Time taken : {t2-t1} sec")
    t1= time.time()
    n=1690
    print(s.nthUglyNumber(n))
    t2=time.time()
    print(f"Time taken : {t2-t1} sec")
