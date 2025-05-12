#URL : https://leetcode.com/problems/finding-3-digit-even-numbers/description/?envType=daily-question&envId=2025-05-12
#[Easy] [2094] 
#Title: [Finding 3-Digit Even Numbers]
#Author: Kartik Bhatnagar
#Date : 2025-05-12 (YYYY-MM-DD)
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digits_len = len(digits)
        result =set()
        for i in range(digits_len):
            if digits[i] == 0:
                continue
            for j in range(digits_len):
                if j == i:
                    continue
                for k in range(digits_len):        
                    if k ==i or j ==k:
                        continue
                    if digits[k] %2 == 0:
                        #the interger is even
                        num = (digits[i]*100)+(digits[j]*10)+(digits[k])
                        result.add(num)
        return sorted(list(result))
if __name__ == "__main__":
    s=Solution()
