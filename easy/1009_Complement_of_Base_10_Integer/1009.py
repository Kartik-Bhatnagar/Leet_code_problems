#URL : https://leetcode.com/problems/complement-of-base-10-integer/description/
#[Easy] [1009] 
#Title: [Complement of Base 10 Integer]
#Author: Kartik Bhatnagar
#Date : 2024-08-22 (YYYY-MM-DD)
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        def deci_to_binary(num)->str:
            b_num =""
            if num==0:
                return "0"
            while num>0:
                b = num%2
                               
                num = num//2
                b_num= str(b)+b_num
                # print(b,num,b_num) 
            return b_num
        def compliment_binary(bnum:str)->str:
            c_b_num=""
            for b in bnum:
                if b=="1":
                    c_b_num +="0"
                else:
                    c_b_num +="1"
            return c_b_num
        def binary_to_deci(bnum):
            base =1
            deci=0
            for b in bnum[::-1]:
                deci = deci+base*int(b)
                base *=2
            return deci

        b_num = deci_to_binary(n)
        c_binary = compliment_binary(b_num)
        deci =binary_to_deci(c_binary)
        # print(c_binary)
        # print(deci) 
        return deci
    
if __name__ == "__main__":
    s=Solution()
    print(s.bitwiseComplement(10))
    print(s.bitwiseComplement(16))
