#URL : https://leetcode.com/problems/count-and-say/description/?envType=daily-question&envId=2025-04-17
#[Medium] [38] 
#Title: [Count and say]
#Author: Kartik Bhatnagar
#Date : 2025-04-18 (YYYY-MM-DD)
class Solution:
    def countAndSay(self, n: int) -> str:
        def rle(num):
            if n == 1:
                return "1"
            ns = str(num)
            prev = ns[0]
            count = 1
            result =""
            for e in range(1,len(ns)):
                if ns[e] == prev:#next occurance is same num
                    count+=1
                else : #next occurance is different num
                    result +=f"{str(count)}{prev}"
                    prev =ns[e]
                    count = 1
            if len(ns) >1:
                result +=f"{str(count)}{ns[e]}"
            else:
                result = f"1{ns}"
            return result
        p ="1"
        for i in range(n-1):            
            p = rle(p)
            # print(p)
        return p
        
if __name__ == "__main__":
    s=Solution()
