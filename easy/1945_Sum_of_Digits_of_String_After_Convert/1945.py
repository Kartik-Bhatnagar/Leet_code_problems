#URL : https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/?envType=daily-question&envId=2024-09-03
#[Easy] [1945] 
#Title: [Sum of Digits of String After Convert]
#Author: Kartik Bhatnagar
#Date : 2024-09-03 (YYYY-MM-DD)
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        d ={ c:str(i+1) for i,c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        conv = [d[c] for c in s]
        conv = "".join(conv)
        conv_sum = sum([int(i) for i in conv])
        print(conv_sum)
        for i in range(k-1):
            conv_sum = sum([int(i) for i in str(conv_sum)])
        return conv_sum
    
if __name__ == "__main__":
    s=Solution()
