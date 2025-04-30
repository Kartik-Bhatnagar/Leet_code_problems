#URL : https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/?envType=daily-question&envId=2025-04-30
#[Easy] [1295] 
#Title: [Find Numbers with Even Number of Digits]
#Author: Kartik Bhatnagar
#Date : 2025-04-30 (YYYY-MM-DD)
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result =0
        def isEven(nm):
            if len(str(nm)) %2 ==0:
                return True
            else:
                return False

        def isEven2(nm):
            cnt = 0
            #given all num are 1 or more
            while nm !=0:
                nm = nm //10
                cnt+=1
            if cnt %2 ==0:
                return True
            else:
                return False
        for num in nums:
            if isEven(num):
                result +=1
        return result
        
if __name__ == "__main__":
    s=Solution()
