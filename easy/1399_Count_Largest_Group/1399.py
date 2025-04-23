#URL : https://leetcode.com/problems/count-largest-group/description/?envType=daily-question&envId=2025-04-23
#[Easy] [1399] 
#Title: [ Count Largest Group]
#Author: Kartik Bhatnagar
#Date : 2025-04-23 (YYYY-MM-DD)
class Solution:
    def countLargestGroup(self, n: int) -> int:
        def digit_sm(num):
            sm =0
            while num:
                m = num%10
                num = num//10
                sm+=m
            return sm
        d =dict()
        max_sm = 0
        for i in range(1,n+1):
            sm = digit_sm(i)#sum([int(st) for st in str(i)])
            d[sm] = d.get(sm,0) +1
            max_sm = max(max_sm,d[sm])
        # print(d)
        result = 0
        for k,v in d.items():
            if v==max_sm:
                result +=1
        return result




        
if __name__ == "__main__":
    s=Solution()
